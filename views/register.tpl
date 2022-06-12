<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Formulario</title>
  <link rel="stylesheet" media="only screen" href="/statics/CSS/style_formulario.css" />
  <script type="text/javascript" rel="stylesheet" src="/statics/JS/espectador-piloto.js"></script>
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
              <legend>¡REGÍSTRATE!</legend>
                  <ul>
                      <li>
                          <label for="nombre">Nombre:</label>
                          <input class="input_texto" type="text" id="nombre" name="nombre">
                      </li>
                      <li>
                          <label for="apellidos">Apellidos:</label>
                          <input class="input_texto" type="text" id="apellidos" name="apellidos">
                      </li>
                      <li>
                          <label for="contraseña">Contraseña:</label>
                          <input class="input_texto" type="password" id="contrasena" name="contrasena">
                      </li>
                      <li>
                      <label for="conf_contraseña">Repetir contraseña:</label>
                      <input class="input_texto" type="password" id="conf_contrasena" name="conf_contraseña_cliente">
                      </li>
                      <li>
                      <label for="email">Email:</label>
                      <input class="input_texto" type="email" id="email" name="email">
                      </li>
                      <li>
                          <label class="input_piloto" for="mail">¿Cómo quiere registrarse?:</label>
                          <br>
                          <input class="boton" type="radio" name="tipo_cliente" id="tipo_cliente" value="piloto" onchange="mostrar(this.value);"> <label>Piloto</label>
                          <input class="boton" type="radio" name="tipo_cliente" id="tipo_cliente" value="espectador" onchange="mostrar(this.value);"> <label>Espectador</label>
                      </li>
                      <div class="espectadores" id="espectadores">
                      <li>
                          <label class="input_piloto">¡Se miembro de nuestro circuito!:</label>
                          <p>- Entradas gratis a todos los eventos</p>
                          <p>-Descuento de un 50% en toda la comida</p>
                          <p>-Descuento en los asientos VIP de un 30%</p>
                          <br>
                          <input class="boton" type="radio" name="espectador_tipo" id="espectador_tipo" value="miembro" onchange="pago(this.value);"> <label>Acepto</label>
                          <input class="boton" type="radio" name="espectador_tipo" id="espectador_tipo" value="no_miembro" onchange="pago(this.value);"> <label>No, gracias</label>
                          <div class="pago" id="pago">
                          <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
                              <input type="hidden" name="cmd" value="_s-xclick">
                              <input type="hidden" name="hosted_button_id" value="P8VGY6FFTGBTW">
                              <input type="image" src="https://www.paypalobjects.com/es_ES/ES/i/btn/btn_subscribeCC_LG.gif" border="0" name="submit" alt="PayPal, la forma rápida y segura de pagar en Internet.">
                              <img alt="" border="0" src="https://www.paypalobjects.com/es_ES/i/scr/pixel.gif" width="1" height="1">
                              </form>
                          </div>                                           
                      </li>
                      <li>
                          <input class="boton_registrarse" id="save_espectador" name="save_espectador" type="submit" value="Registrarse">  
                      </li>
                      </div>
                      <div class="pilotos" id="pilotos">
                          <li>
                              <input class="boton_registrarse" id="save_piloto" name="save_piloto" type="submit" value="Registrarse">
                          </li>

                      </div>                      
                  </ul>
              </fieldset>
          </form>
          </div>
      </div>
  </div>
</body>