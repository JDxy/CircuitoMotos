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