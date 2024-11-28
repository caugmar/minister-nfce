import chevron
from weasyprint import HTML

def generate_report(nfce_data, template_file, output_pdf):
    with open(template_file, "r") as f:
        template = f.read()
    rendered_html = chevron.render(template, nfce_data)
    HTML(string=rendered_html).write_pdf(output_pdf)
