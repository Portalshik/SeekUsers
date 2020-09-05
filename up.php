<?php
$seek = file_get_contents("https://github.com/Portalshik/SeekUsers/blob/master/seek_users.py");
$file = fopen("seek_user.py", "w");
fwrite($file, $seek);
fclose($file);
?>
