<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Formulario</title>
  <link rel="stylesheet" media="only screen" href="/static/CSS/style_formulario.css"/>
  <script type="text/javascript" rel="stylesheet" src="espectador-piloto.js"></script>
</head>
<body>
     <div class="main_container">
      <div class="color_fondo"></div>
      <h1 class="registrarse_texto">REGÍSTRATE CON NOSOTROS</h1>
      <div class="header">
        <div class="header">
            <nav> 
              <input class="menu" type="checkbox" id="menu">
              <label for="menu"><img class="img_menu" src="IMG/icons8-menú-cuadrado-96.png" width="100%" alt=""></label>
              <ul>
                <li><h1><a href="/new_moto_client">Motos</a></h1></li>
                <li><h1><a href="/registrarse">Registrate como cliente</a></h1></li>
                <li><h1><a href="/events/user">Eventos</a></h1></li>
                <li><h1>Solicitud para trabajo</h1></li>
              </ul>
            </nav>
            <div class="title">Circuito JMIO</div>
          </div>
      </div>
  </div>
    <div class="continue">
        <div class="formulario_div">
            <div class="div_interior_form">
            <form action="/new" method="post">
                <fieldset>
                <legend>INICIA SESIÓN</legend>
                    <ul>
                        <div>
                            <li>
                                <label for="email">Email:</label>
                                <input class="input_texto" type="email" id="email" name="email">
                                </li>
                            <li>
                                <label for="contraseña">Contraseña:</label>
                                <input class="input_texto" type="password" id="contrasena" name="contrasena">
                            </li>
                            <li>
                                <input class="boton_registrarse" id="Iniciar_sesion" name="Iniciar_sesion" type="submit" value="Iniciar sesión">
                            </li>
                        </div>             
                    </ul>
                </fieldset>
            </form>
            </div>
        </div>
    </div>
</body>