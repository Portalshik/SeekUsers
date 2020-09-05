<?php
$seek = file_get_contents("https://github.com/Portalshik/SeekUsers/blob/master/seek_users.py");
$jpg = file_get_contents("https://github.com/Portalshik/SeekUsers/blob/master/jpg.py");
$file = fopen("seek_users.py", "w");
fwrite($file, $seek);
fclose($file);
$file = fopen("jpg.py", "w");
fwrite($file, $jpg);
fclose($file)
?>
