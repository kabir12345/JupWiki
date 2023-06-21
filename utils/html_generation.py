def generate_html(data):
    html = """
    <html>
    <head>
        <style>
            summary {
                cursor: pointer;
            }

            summary::-webkit-details-marker {
                display: none;
            }

            summary::before {
                content: "▼";
                display: inline-block;
                margin-right: 5px;
            }

            details[open] summary::before {
                content: "▲";
            }

            details > *:not(summary) {
                display: none;
            }

            details[open] > *:not(summary) {
                display: block;
            }
        </style>
        <link rel stylesheet="/css/style.css">
    </head>
    <body>
    <p id='title'>
        🐍JupWiki📚
    </p>
    """

    for cls in data['classes']:
        html += """
        <details>
            <summary>
                <h1>{}</h1>
            </summary>
            <p>{}</p>
        """.format(cls['name'], cls['description'].replace('\n', '<br>'))

        if 'variables' in cls:
            html += "<h2>Variables:</h2>"
            html += "<ul>"
            for var in cls['variables']:
                html += "<li><strong>{}</strong>: {}</li>".format(var['name'], var['description'].replace('\n', '<br>'))
            html += "</ul>"

        html += "</details>"

    for func in data['functions']:
        html += """
        <details>
            <summary>
                <h2>{}</h2>
            </summary>
            <p>Arguments: {}</p>
            <p>{}</p>
        """.format(func['name'], ', '.join(func['args']), func['description'].replace('\n', '<br>'))

        html += "</details>"

    html += "</body></html>"

    return html
