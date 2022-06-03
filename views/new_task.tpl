<p>Añadir una nueva tarea a la lista:</p>
<form action="/new" method="POST">
    <input type="text" size="100" maxlength="100" name="Fecha_inicio">
    <input type="text" size="100" maxlength="100" name="Fecha_fin">
    <input type="text" size="100" maxlength="100" name="Categoria">
    <input type="decimal" size="100" maxlength="100" name="Coste_participantes">
    <input type="decimal" size="100" maxlength="100" name="Coste_espectadores">
    <input type="submit" name="save" value="save">
</form>