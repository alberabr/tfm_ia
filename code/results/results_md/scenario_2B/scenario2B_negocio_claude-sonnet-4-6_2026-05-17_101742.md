# Gestión de una Exposición de Datos en Entidad Financiera

## Evaluación inicial honesta

Antes de entrar en el plan, es importante que tengas claro algo: **la gestión transparente y diligente protege más la reputación que intentar minimizar o retrasar**. Los casos que han generado mayor daño reputacional suelen ser aquellos donde se detectó ocultación o tardanza injustificada.

---

## Fase 1: Contención inmediata (primeras horas)

**Acciones técnicas urgentes:**
- Cerrar el acceso público al repositorio **de inmediato** si no se ha hecho ya
- Preservar logs y evidencias **sin modificarlos** (crítico para el análisis forense)
- Aislar el sistema si hay indicios de compromiso activo
- Revocar credenciales potencialmente expuestas

**Activar internamente:**
- Equipo de respuesta a incidentes (CSIRT/SOC)
- Responsable de Seguridad de la Información (CISO)
- Delegado de Protección de Datos (DPO) — **obligatorio bajo RGPD**
- Asesoría jurídica
- Dirección general

---

## Fase 2: Análisis forense del alcance real

Esto es lo más importante antes de tomar decisiones de comunicación:

**Qué necesitas determinar:**
- ¿Qué datos estaban expuestos? (categorías, volumen, sensibilidad)
- ¿Durante cuánto tiempo estuvo accesible?
- ¿Hay evidencia de acceso externo? (logs de acceso, IPs, descargas)
- ¿Qué clientes están afectados y cuántos?
- ¿Incluye datos especialmente protegidos? (datos financieros, documentación de identidad)

**Herramientas de análisis:**
- Revisión exhaustiva de logs de acceso
- Análisis de tráfico de red del período
- Búsqueda en fuentes OSINT y dark web de datos filtrados
- Peritos forenses externos si la capacidad interna es insuficiente

---

## Fase 3: Obligaciones regulatorias — No son opcionales

### RGPD (Reglamento General de Protección de Datos)
| Obligación | Plazo | Condición |
|------------|-------|-----------|
| Notificar a la AEPD | **72 horas** desde conocimiento | Si hay riesgo para derechos de personas |
| Notificar a afectados | Sin dilación indebida | Si hay riesgo **alto** para sus derechos |
| Documentar el incidente | Siempre | Independientemente del riesgo |

> ⚠️ El plazo de 72 horas corre desde que tienes **conocimiento razonable**, no desde que completas la investigación. Puedes notificar con información parcial e ir completando.

### Regulación financiera específica
- **Banco de España / BCE**: Notificación según normativa de resiliencia operacional
- **CNMV** si aplica según el tipo de entidad
- **DORA** (si ya está en vigor para tu entidad): obligaciones adicionales de reporte
- Revisar obligaciones contractuales con clientes institucionales

---

## Fase 4: Estrategia de comunicación

### Principios que deben guiarla:
- **Proactividad** sobre reactividad
- **Precisión** sobre generalización (no comunicar más ni menos de lo que sabes)
- **Acciones concretas** sobre disculpas genéricas

### Secuencia recomendada:
1. **Reguladores** — primero y dentro de plazo legal
2. **Clientes afectados** — comunicación directa, personalizada, con medidas de protección ofrecidas
3. **Comunicación pública** — solo si hay filtración mediática o el regulador lo requiere
4. **Empleados** — para que no sean sorprendidos por noticias externas

### Qué debe incluir la comunicación a afectados:
- Qué ocurrió (sin tecnicismos innecesarios)
- Qué datos estuvieron expuestos
- Qué evidencia hay (o no hay) de uso indebido
- Qué medidas habéis tomado
- Qué pueden hacer ellos para protegerse
- Canal de contacto dedicado

---

## Fase 5: Gestión del riesgo reputacional

**Lo que realmente protege la reputación:**

✅ Actuar rápido y documentarlo  
✅ Ser transparente con reguladores  
✅ Comunicar a afectados antes de que lo lean en prensa  
✅ Ofrecer medidas concretas (monitorización de crédito, etc.)  
✅ Explicar qué cambios sistémicos se implementan  

❌ Lo que la destruye: retrasos injustificados, minimización pública desmentida después, que los afectados se enteren por terceros

---

## Fase 6: Revisión post-incidente

Una vez gestionada la crisis:
- Análisis de causa raíz (¿cómo quedó expuesto el repositorio?)
- Auditoría de otros repositorios y sistemas similares
- Revisión de controles de acceso y monitorización
- Plan de mejora con responsables y plazos
- Formación si hubo factor humano

---

## Resumen de prioridades inmediatas

```
HOY:
□ Contener el acceso
□ Preservar evidencias
□ Activar DPO y asesoría jurídica
□ Iniciar análisis forense

EN 72 HORAS:
□ Evaluar obligación de notificación a AEPD
□ Determinar alcance preliminar
□ Preparar comunicación a afectados si procede

ESTA SEMANA:
□ Completar análisis forense
□ Comunicar a afectados
□ Plan de mejora de controles
```

---

¿Quieres que profundice en algún aspecto concreto: el proceso de notificación a la AEPD, la redacción de la comunicación a clientes, o el análisis técnico forense?