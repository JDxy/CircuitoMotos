<p>Añadir una nueva tarea a la lista:</p>
<form action="/new" method="POST">
    <p>Fecha_inicio</p>
    <input type="text" size="100" maxlength="100" name="Fecha_inicio">
    <p>Fecha_fin</p>
    <input type="text" size="100" maxlength="100" name="Fecha_fin">
    <p>Categoria</p>
    <input type="text" size="100" maxlength="100" name="Categoria">
    <p>Coste_participantes</p>
    <input type="decimal" size="100" maxlength="100" name="Coste_participantes">
    <p>Coste_espectadores</p>
    <input type="decimal" size="100" maxlength="100" name="Coste_espectadores">
    <input type="submit" name="save" value="save">
</form>