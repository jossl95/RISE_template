from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import execute
import nbformat
import re


# Taken from:
# https://stackoverflow.com/questions/35805121/execute-a-jupyter-notebook-including-inline-markdown-with-nbconvert
class ExecuteCodeMarkdownPreprocessor(ExecutePreprocessor):

    def __init__(self, **kw):
        self.sections = {'default': True} # maps section ID to true or false
        self.EmptyCell = nbformat.v4.nbbase.new_raw_cell("")

        super().__init__(**kw)

    def preprocess_cell(self, cell, resources, cell_index, store_history=True):
        """
        Executes a single code cell. See base.py for details.
        To execute all cells see :meth:`preprocess`.
        """

        if cell.cell_type not in ['code', 'markdown']:
            return cell, resources

        if cell.cell_type == 'code':
            # Do code stuff
            return self.preprocess_code_cell(cell, resources, cell_index, store_history)

        elif cell.cell_type == 'markdown':
            # Do markdown stuff
            return self.preprocess_markdown_cell(cell, resources, cell_index, store_history)
        else:
            # Don't do anything
            return cell, resources

    def preprocess_code_cell(self, cell, resources, cell_index, store_history):
        """ Process code cell.
        """
        # outputs = self.run_cell(cell)
        reply, outputs = self.run_cell(cell, cell_index, store_history)

        cell.outputs = outputs

        cell_allows_errors = (self.allow_errors or "raises-exception"
                              in cell.metadata.get("tags", []))

        if self.force_raise_errors or not cell_allows_errors:
            for out in cell.outputs:
                if out.output_type == 'error':
                    raise execute.CellExecutionError.from_cell_and_msg(cell, out)
            if (reply is not None) and reply['content']['status'] == 'error':
                raise execute.CellExecutionError.from_cell_and_msg(cell, reply['content'])

        return cell, resources

    def preprocess_markdown_cell(self, cell, resources, cell_index, store_history):
        # Find and execute snippets of code
        cell['metadata']['variables'] = {}
        for m in re.finditer("{{(.*?)}}", cell.source):
            # Execute code
            fakecell = nbformat.v4.nbbase.new_code_cell(m.group(1))
            fakecell, resources = self.preprocess_code_cell(fakecell, resources, cell_index, store_history)

            # Output found in cell.outputs
            # Put output in cell['metadata']['variables']
            for output in fakecell.outputs:
                html = self.convert_output_to_html(output)
                if html is not None:
                    cell['metadata']['variables'][fakecell.source] = html
                    break
        return cell, resources

    def convert_output_to_html(self, output):
        """Convert IOpub output to HTML

        See https://github.com/ipython-contrib/IPython-notebook-extensions/blob/master/nbextensions/usability/python-markdown/main.js
        """
        if output['output_type'] == 'error':
            text = '**' + output.ename + '**: ' + output.evalue
            return text
        elif output.output_type == 'execute_result' or output.output_type == 'display_data':
            data = output.data
            if 'text/latex' in data:
                html = data['text/latex']
                return html
            elif 'image/svg+xml' in data:
                # Not supported
                #var svg = ul['image/svg+xml'];
                #/* embed SVG in an <img> tag, still get eaten by sanitizer... */
                #svg = btoa(svg);
                #html = '<img src="data:image/svg+xml;base64,' + svg + '"/>';
                return None
            elif 'image/jpeg' in data:
                jpeg = data['image/jpeg']
                html = '<img src="data:image/jpeg;base64,' + jpeg + '"/>'
                return html
            elif 'image/png' in data:
                png = data['image/png']
                html = '<img src="data:image/png;base64,' + png + '"/>'
                return html
            elif 'text/markdown' in data:
                text = data['text/markdown']
                return text
            elif 'text/html' in data:
                html = data['text/html']
                return html
            elif 'text/plain' in data:
                text = data['text/plain']
                # Strip <p> and </p> tags
                # Strip quotes
                # html.match(/<p>([\s\S]*?)<\/p>/)[1]
                text = re.sub(r'<p>([\s\S]*?)<\/p>', r'\1', text)
                text = re.sub(r"'([\s\S]*?)'",r'\1', text)
                return text
            else:
            # Some tag we don't support
                return None
        else:
            return None