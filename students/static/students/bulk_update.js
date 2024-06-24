<!DOCTYPE html>
<html>
<head>
    <title>Upload CSV</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        #progress-circle {
            display: none;
            border: 16px solid #f3f3f3;
            border-radius: 50%;
            border-top: 16px solid #3498db;
            width: 120px;
            height: 120px;
            animation: spin 2s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <h1>Upload CSV</h1>
    <button id="download-template">Download Template</button>
    <form id="upload-form" enctype="multipart/form-data">
        <input type="file" id="file-input" name="file" accept=".csv">
        <button type="submit">Upload</button>
    </form>
    <div id="progress-circle"></div>

    <script>
        $(document).ready(function() {
            $('#download-template').click(function() {
                window.location.href = '/download-template/';
            });

            $('#upload-form').on('submit', function(e) {
                e.preventDefault();
                var formData = new FormData(this);
                $('#progress-circle').show();

                $.ajax({
                    url: '/bulk-upload/',
                    type: 'POST',
                    data: formData,
                    processData: false,
                    contentType: false,
                    success: function(response) {
                        alert(response.message);
                        $('#progress-circle').hide();
                    },
                    error: function(xhr) {
                        alert('An error occurred: ' + xhr.responseText);
                        $('#progress-circle').hide();
                    }
                });
            });
        });
    </script>
</body>
</html>
