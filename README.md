# Bot Telegram para The Hive
Este proyecto es un fork del proyecto de Santi Fernandez.<p>
Este es un  bot hecho en Python que se comunica mediante la api de THE HIVE y podes hacer lo siguiente:

1.Obtener las alertas no leidas<p>
2.Leer alertas<p>
3.Promover alertas a casos especificos con los template creados en la plataforma de The Hive<p>


Algunos comentarios para que funcione: <p>
Se debe tener un bot de telegram y configurar el token del mismo. <p>
Ademas se debe tener la api key y url para comunicarse con la plataforma The Hive<p>
Los comandos disponibles son: <p>
/start<p>
/leerAlertas<p>
/alertas<p>
/crearCasoPhish<p>
/crearIncidente<p>

Los pasos para ejecutarlo son : <p>
#docker build -t hivebot . <p>
#docker run -e TOKEN_TELEGRAM="YOUR_TELEGRAM_TOKEN"  hivebot <p>

Tambien se debe configurar el chat id ! <p>

Comentarios bienvenidos!<p>
Sientanse libres de clonarlo y usarlo!<p>
