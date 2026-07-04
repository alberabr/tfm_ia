Esta es una situación crítica, especialmente en el sector financiero debido a la regulación y la sensibilidad de los datos. Como analista de seguridad, tu prioridad debe ser **contener el daño, evaluar el alcance y asegurar la continuidad del negocio** siguiendo un protocolo de Respuesta a Incidentes (IR).

Aquí tienes una hoja de ruta de acciones inmediatas dividida por fases:

### 1. Contención Inmediata (Frenar la propagación)
No esperes a tener toda la información para actuar sobre lo que ya sabes que está infectado.
*   **Aislamiento de red:** Desconecta de la red (físicamente o mediante VLANs de cuarentena) los sistemas afectados. **No los apagues** si es posible, ya que podrías borrar pruebas en la memoria RAM (artefactos del malware, claves de cifrado).
*   **Bloqueo de cuentas:** Deshabilita temporalmente las cuentas de administrador de dominio y cuentas de servicio que sospeches comprometidas.
*   **Cierre de conexiones externas:** Corta accesos VPN y conexiones RDP hacia el exterior.
*   **Preservar copias de seguridad:** Asegúrate de que tus backups (offline o inmutables) estén desconectados de la red para que el ransomware no los cifre también.

### 2. Análisis y Triaje (Entender el alcance)
*   **Identificar el "Paciente Cero":** Revisa logs de EDR, SIEM y firewalls para ver cómo entró (phishing, vulnerabilidad en VPN, RDP expuesto).
*   **Determinar la variante:** Si hay una nota de rescate, identifica la familia del ransomware. Esto te dirá si suelen exfiltrar datos (doble extorsión) o solo cifrar.
*   **Inventario de daños:** Clasifica los sistemas en:
    *   Confirmados como cifrados.
    *   Sospechosos (comportamiento anómalo).
    *   Limpios (aislar preventivamente).
*   **Verificar exfiltración:** Busca picos de tráfico de salida inusuales en los días/horas previos al incidente. Esto es vital para saber si hay brecha de datos personales (GDPR/LOPD).

### 3. Comunicación y Escalado (Obligatorio en Sector Financiero)
Al ser una entidad financiera, los tiempos y las formas son críticos:
*   **Comité de Crisis:** Notifica inmediatamente al CISO, CTO y al departamento Legal.
*   **Reguladores:** Dependiendo de tu país, podrías tener una ventana de pocas horas (ej. 72h para GDPR, o plazos específicos de la normativa **DORA** en la UE o el Banco Central correspondiente) para notificar el incidente.
*   **Comunicación a Clientes:** Si la plataforma de pagos está caída, el equipo de PR/Comunicación debe preparar un mensaje oficial para evitar el pánico, sin dar detalles técnicos que ayuden al atacante.

### 4. Erradicación y Recuperación
*   **No pagues el rescate:** No hay garantías de recuperar los datos y financias el cibercrimen. Además, para entidades financieras, pagar puede suponer sanciones legales.
*   **Limpieza profunda:** No basta con borrar el malware. Debes reinstalar sistemas desde imágenes limpias o backups verificados.
*   **Cambio de credenciales:** Resetea TODAS las contraseñas de la infraestructura (Active Directory, bases de datos, firewalls).
*   **Parcheo:** Antes de volver a poner un sistema online, asegúrate de que la vulnerabilidad por la que entraron esté parcheada.

### 5. Consideraciones Legales y Forenses
*   **Cadena de custodia:** Si planeas denunciar (lo cual es recomendable), asegúrate de que las imágenes de disco y logs se recojan de forma forense.
*   **Seguro de Ciberriesgo:** Si la entidad tiene uno, llámalos ya. Ellos suelen poner a tu disposición equipos de respuesta a incidentes especializados.

### Resumen de prioridades para TI ahora mismo:
1.  **Aislar** la plataforma de pagos del resto de la red corporativa.
2.  **Verificar la integridad de los backups.**
3.  **Determinar si hubo robo de datos** (esto cambia la gravedad legal del asunto).

**¿Tienes visibilidad sobre el EDR o el SIEM en este momento?** Si ves procesos sospechosos o conexiones a IPs externas desconocidas, empieza por ahí el bloqueo.