Si hay **accesos sospechosos con cuentas de administrador en un banco**, debes tratarlo como un **incidente grave de ciberseguridad** con posible impacto operativo, regulatorio y sobre clientes.

## Qué hacer de inmediato
1. **Activa el procedimiento interno de respuesta a incidentes** de tu entidad.
   - Contacta **ya** con:
     - **CISO / Seguridad de la Información / SOC**
     - **Equipo de respuesta a incidentes / IT Security**
     - **Responsable de continuidad / operaciones**
     - **Cumplimiento normativo / DPO / asesoría jurídica**
     - **Dirección** según el protocolo interno

2. **Escala el incidente como prioridad alta/crítica**.
   - Aunque no sepas aún el alcance, el uso sospechoso de cuentas privilegiadas implica riesgo elevado.

3. **Preserva evidencias**.
   - No borres logs, no reinicies sistemas sin indicación del equipo forense, no “limpies” equipos por tu cuenta.
   - Documenta:
     - fecha y hora de detección
     - quién informó
     - cuentas afectadas
     - sistemas donde se observó actividad
     - acciones ya realizadas

4. **Contén el riesgo con criterio técnico**.
   - Si una cuenta de administrador parece comprometida, normalmente debe **aislarse, deshabilitarse o rotarse credenciales** cuanto antes.
   - Si hay cuentas críticas para operación, no decidas tú solo mantenerlas activas: esto debe valorarlo **Seguridad + Operaciones + responsables del servicio** con medidas compensatorias inmediatas:
     - supervisión reforzada
     - restricción de accesos
     - cambio de credenciales
     - MFA
     - uso temporal de cuentas alternativas controladas
     - segmentación o aislamiento

5. **Verifica posible impacto en clientes y datos**.
   - Pide al equipo técnico que determine:
     - qué sistemas fueron accedidos
     - desde cuándo
     - qué privilegios se usaron
     - si hubo acceso, copia, modificación o exfiltración de datos
     - si afecta a banca online, pagos, core bancario, CRM, correo, AD, backups, etc.

## A quién avisar
### Internamente
- **Seguridad de la información / SOC / CSIRT interno**
- **CISO**
- **Responsable de IT / Infraestructura**
- **Dirección de la sucursal**, si el protocolo lo exige
- **Cumplimiento / Riesgos / Auditoría interna**
- **DPO / Privacidad**, si puede haber datos personales
- **Asesoría jurídica**
- **Continuidad de negocio**

### Externamente
Depende del país y del alcance, pero en general un banco puede tener obligación de notificar a:
- **Autoridad supervisora financiera** correspondiente
- **Autoridad de protección de datos**, si hay brecha de datos personales
- **CERT/CSIRT nacional o sectorial**
- **Fuerzas y cuerpos de seguridad**, si procede
- **Proveedores críticos** afectados o implicados

Si me dices el **país**, puedo indicarte **qué organismos concretos** suelen notificarse y en qué casos.

## Qué no hacer
- No ignores el incidente porque “no está confirmado”.
- No mantengas cuentas privilegiadas sospechosas activas solo por comodidad operativa sin aprobación formal.
- No comuniques a clientes ni terceros por tu cuenta sin coordinación con legal/compliance/comunicación.
- No alteres evidencias.
- No uses canales informales para compartir detalles sensibles.

## Criterio práctico
Si tú no eres el responsable técnico de ciberseguridad, tu papel inmediato es:
1. **escalar**
2. **documentar**
3. **seguir el plan interno**
4. **asegurar que seguridad, legal y dirección estén informados**

## Mensaje breve que puedes enviar internamente
> “Se han detectado accesos sospechosos a sistemas internos mediante cuentas con privilegios de administrador. En este momento se desconoce el alcance, los sistemas afectados y si existe impacto sobre datos o clientes. Solicito activación inmediata del procedimiento de respuesta a incidentes, análisis urgente por Seguridad/SOC y valoración de medidas de contención, preservando evidencias y coordinando con Cumplimiento, DPO y Dirección.”

Si quieres, puedo ayudarte a redactar:
- un **correo de escalado interno**
- un **checklist de las primeras 2 horas**
- o una **matriz de a quién avisar según si hubo datos de clientes o no**.