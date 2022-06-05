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
    </tr>
  %end
</table>