
<?php
	try{
		if (!file_exists('anti_ddos/start.php'))
			throw new Exception ('anti_ddos/start.php does not exist');
		else
			require_once('anti_ddos/start.php'); 
	} 
	//CATCH the exception if something goes wrong.
	catch (Exception $ex) {
		echo '<div style="padding:10px;color:white;position:fixed;top:0;left:0;width:100%;background:black;text-align:center;">'.
			'The <a href="https://github.com/yuhertz/cybersecurity" target="_blank">"AntiDDOS System"</a> failed to load '.
			'properly on this Web Site, please de-comment the \'catch Exception\' to see what happening!</div>';
		//Print out the exception message.
		//echo $ex->getMessage();
	}
?>

<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" href="css/flottant.css">
		<title>Example Webpage</title>
	</head>
	<body>
		<center>
			<div class="container">
				<a href="https://github.com/yuhertz">
				</a>
				<h1>Example Webpage</h1>
				<p>This web Site is protected by AntiDDOS-System PHP.</p>
			</div>
		</center>
	</body>
</html>
