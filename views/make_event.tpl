<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>events</title>
  <link rel="stylesheet" media="only screen" href="/statics/CSS/style_event.css"/>
  <link rel="icon" type="image/icon" href="/statics/IMG/JMIO PRINCIPAL (1).ico"/>
</head>

<body>
<div class="main_container">

  <div class="header">
   
    <nav> 
      <input type="checkbox" id="menu">
      <label for="menu"><img class="img_menu" src="IMG/icons8-menú-cuadrado-96.png" width="100%" alt=""></label>
      <ul>
        <li><h1>Motos</h1></li>
        <li><h1>Registrate como cliente</h1></li>
        <li><h1>Nuestro cliente</h1></li>
        <li><h1>Solicitud para trabajo</h1></li>
      </ul>
    </nav>
    <div class="title">Circuito JMIO</div>
  </div>

  <img class="First_IMG" src="/statics/IMG/3.jpg" alt="">
  
  <section class="section_1">
    <h1>Eventos</h1>
<table border="1">

<tr>
    <th>ID</th>
    <th>Fecha de inicio</th>
    <th>Fecha de fin</th>
    <th>categoria</th>
    <th>coste participantes</th>
    <th>coste espectadores</th>
</tr>
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end


  <td>
    <form action="/edit/{{row[0]}}" method="GET">
        <input type="submit" name="save" value="Editar">
    </form>
  </td>
  <td>
    <form action="/delete/{{row[0]}}" method="GET">
        <input type="submit" name="delete" value="Borrar">
    </form>
  </td>
  %end
  </tr>
    <form action="/new" method="GET">
    <input type="submit" name="new" value="Incluir">
    </form>
</table>
    </section>

</body>

</html>