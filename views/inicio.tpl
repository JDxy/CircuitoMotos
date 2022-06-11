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
        <h1 class="registrarse_texto">BIENVENIDO DE VUELTA</h1>
        <div class="header">
            <nav> 
                <input type="checkbox" id="menu">
                <label for="menu"><img class="img_menu" src="IMG/icons8-menú-cuadrado-96.png" width="100%" alt="">  </label>
                <ul>
                <li>
                    <div class="flip-card-menu">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                        <img src="IMG/suzuki-hybrid-gsx-r-p.jpg" alt="Avatar">
                        </div>
                        <div class="flip-card-back">
                        <h1>Motos</h1> 
                        </div>
                    </div>
                    </div>
                </li>
                <li>
                    <div class="flip-card-menu">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                        <img src="IMG/artculo-expectativas-clientes.png" alt="Avatar">
                        </div>
                        <div class="flip-card-back">
                        <h1>Registrate como cliente</h1> 
                        </div>
                    </div>
                    </div>
                </li>
                <li>
                    <div class="flip-card-menu">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                        <img src="IMG/circuito-de-las-americas-austin-motogp_cg4oamgh4uhp1fk3d7r2yb9j4.png" alt="Avatar">
                        </div>
                        <div class="flip-card-back">
                        <h1>Nuestro circuito</h1> 
                        </div>
                    </div>
                    </div>
                </li>
                <li>
                    <div class="flip-card-menu">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                        <img src="IMG/3.jpg" alt="Avatar">
                        </div>
                        <div class="flip-card-back">
                        <h1>Eventos</h1> 
                        </div>
                    </div>
                    </div>
                </li>
                </ul>
            </nav>
            <div class="title">Circuito JMIO</div>
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