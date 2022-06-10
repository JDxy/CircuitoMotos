<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mostrar tabla</title>
</head>
<body>
    <p>Añadir una nueva tarea a la lista:</p>
    <form action="/new" method="POST">
        <input type="text" size="100" maxlength="100" name="task">
        <input type="submit" name="save" value="save">
    </form>
 

        
    %#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
    <p>Las tareas pendientes son las siguientes:</p>
    <table border="1">
        <td>ID</td><td>Tareas</td><td>Estado</td><td>Acciones</td>
        %for row in rows:
        <tr>
        %for i in range(len(row)):
       
            %if i == 2:
                %if row[i] == 0:

                    <td>Cerrada</td><td><button>editar</button></td>
                    %else:
                    <td>Abierto</td><td><button>editar</button><form action="/delete/{{count}}" method="POST">        
        <input type="submit" name="delete" value="Borrar">
    </form></td>
                %end
            %else:
                <td>{{row[i]}}</td>
            %end
        %end
        </tr>
        <tr>
            
        </tr>
        %end
    </table>
</body>
</html>