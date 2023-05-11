<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
	<link rel="stylesheet" type="text/css" href="styles.css">
	<title>File Upload</title>
</head>
<body>
	<div class="outer-box">
		<div class="inner-box">
			<h3 class="text-center">File Upload</h3>
			<form action="upload.php" method="POST" enctype="multipart/form-data">
				<div class="input-group mt-4">
  					<input type="file" name="file" class="form-control" id="inputGroupFile04" aria-describedby="inputGroupFileAddon04" aria-label="Upload">
  					<button class="btn btn-outline-secondary" type="submit" name="submit" id="inputGroupFileAddon04">Upload!</button>
				</div>
			</form>
		</div>
	</div>
</body>
</html>