<?php
$seek = file_get_contents("https://raw.githubusercontent.com/Portalshik/SeekUsers/master/seek_users.py");
$jpg = file_get_contents("https://raw.githubusercontent.com/Portalshik/SeekUsers/master/jpg.py");
$file = fopen("seek_users.py", "w");
fwrite($file, $seek);
fclose($file);
$file = fopen("jpg.py", "w");
fwrite($file, $jpg);
fclose($file)
?>
