<?php 
	
	if (isset($_POST['submit'])) {
		$file = $_FILES['file'];

		$fileName = $file['name'];
		$fileTmpName = $file['tmp_name'];
		$fileSize = $file['size'];
		$fileError = $file['error'];
		$fileType = $file['type'];

		$fileExt = explode('.', $fileName);
		if (in_array('png', $fileExt)) {
			if ($fileError === 0) {
				if ($fileSize < 1000) {
					$fileDest = 'uploads/'.$fileName;
					move_uploaded_file($fileTmpName, $fileDest);
					echo "File uploaded successfully.";
				} else {
					echo "File too large!";
				}
			} else {
				echo "Error in uploading files.";
			}
		} else {
			echo "Only PNGs are allowed!";
		}
	}