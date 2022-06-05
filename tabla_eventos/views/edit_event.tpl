<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar evento</title>
</head>
<body>
    <p>Editar el evento número = {{no}}</p>
    <form action="/edit/{{no}}" method="POST">
      <p>Fecha_inicio</p>
      <input type="text" name="Fecha_inicio" size="100" maxlength="100">
      <p>Fecha_fin</p>
      <input type="text" name="Fecha_fin" size="100" maxlength="100">
      <p>Categoria</p>
      <input type="text" name="Categoria" size="100" maxlength="100">
      <p>Coste_participantes</p>
      <input type="Decimal" name="Coste_participantes" size="100" maxlength="100">
      <p>Coste_espectadores</p>
      <input type="Decimal" name="Coste_espectadores" size="100" maxlength="100">
      <br>
      <input type="submit" name="save" value="save">
    </form>   
</body>
</html>