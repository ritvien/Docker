async def get_html():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gender Prediction</title>
    </head>
    <body>
        <h1>Upload an image for gender prediction</h1>
        <form id="uploadForm" enctype="multipart/form-data">
            <input type="file" id="fileInput" name="file" accept="image/*" />
            <button type="submit">Upload</button>
        </form>
        <h3 id="result"></h3>
        <script>
            const form = document.getElementById("uploadForm");
            form.addEventListener("submit", async (event) => {
                event.preventDefault();
                const fileInput = document.getElementById("fileInput");
                const formData = new FormData();
                formData.append("file", fileInput.files[0]);

                try {
                    const response = await fetch('/predict-gender/', {
                        method: 'POST',
                        body: formData,
                    });
                    const result = await response.json();
                    document.getElementById("result").innerText = 'Predicted gender: ' + result.gender;
                } catch (error) {
                    document.getElementById("result").innerText = 'Error: ' + error.message;
                }
            });
        </script>
    </body>
    </html>
    """
    return html_content