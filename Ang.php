<form method="post" action="">
<input type="number" name="angka" >
<input type="number" name="angka1" >
<input type="submit" >
</form>

<?php 
 $ang = $_POST["angka"];
 $ang1 = $_POST["angka1"];
 $h = $ang + $ang1;
echo "$h";
?>