# Contenido de las guías. Datos verificados el 9/10/2026 en fuentes oficiales
# (tabla de ARCA "Valores de aplicación desde el 1/08/2026"). Cuando ARCA publique
# la tabla nueva (febrero 2027), actualizar CATEGORIAS, ACTUALIZADO y regenerar.

ACTUALIZADO = 'octubre de 2026'
ACTUALIZADO_ISO = '2026-10-09'
VIGENCIA = 'valores vigentes desde el 1 de agosto de 2026'

ARCA_CATEGORIAS = ('ARCA — Categorías y montos', 'https://www.afip.gob.ar/monotributo/categorias.asp')

# Cat, ingresos brutos anuales, superficie, energía, alquileres, imp. integrado (serv/venta), SIPA, obra social, total (serv/venta)
CATEGORIAS = [
    ('A', '12.009.410,45', '30 m²', '3.330 kW', '2.792.886,15', '5.585,77', '5.585,77', '18.246,86', '25.694,55', '49.527,18', '49.527,18'),
    ('B', '17.595.182,74', '45 m²', '5.000 kW', '2.792.886,15', '10.612,98', '10.612,98', '20.071,55', '25.694,55', '56.379,08', '56.379,08'),
    ('C', '24.670.494,31', '60 m²', '6.700 kW', '3.816.944,41', '18.246,86', '16.757,32', '22.078,71', '25.694,55', '66.020,12', '64.530,58'),
    ('D', '30.628.651,43', '85 m²', '10.000 kW', '3.816.944,41', '29.790,79', '27.742,67', '24.286,58', '30.535,56', '84.612,93', '82.564,81'),
    ('E', '36.028.231,33', '110 m²', '13.000 kW', '4.841.002,66', '55.857,73', '44.313,79', '26.715,24', '37.238,48', '119.811,45', '108.267,51'),
    ('F', '45.151.659,41', '150 m²', '16.500 kW', '4.841.002,66', '78.573,20', '57.719,64', '29.386,76', '42.824,25', '150.784,21', '129.930,65'),
    ('G', '53.995.798,87', '200 m²', '20.000 kW', '5.771.964,69', '142.995,76', '71.497,87', '41.141,46', '46.175,72', '230.312,94', '158.815,05'),
    ('H', '81.924.660,37', '200 m²', '20.000 kW', '8.378.658,45', '409.623,31', '204.811,64', '57.598,04', '55.485,33', '522.706,68', '317.895,01'),
    ('I', '91.699.761,90', '200 m²', '20.000 kW', '8.378.658,45', '814.591,79', '325.836,71', '80.637,26', '68.518,81', '963.747,86', '474.992,78'),
    ('J', '105.012.519,20', '200 m²', '20.000 kW', '8.378.658,45', '977.510,14', '391.004,07', '112.892,16', '76.897,46', '1.167.299,76', '580.793,69'),
    ('K', '126.610.838,75', '200 m²', '20.000 kW', '8.378.658,45', '1.368.514,20', '456.171,40', '158.049,02', '87.882,82', '1.614.446,04', '702.103,24'),
]


def tabla_topes():
    filas = ''.join(f'<tr><td><strong>{c[0]}</strong></td><td>${c[1]}</td><td>${c[9]}</td><td>${c[10]}</td></tr>' for c in CATEGORIAS)
    return ('<div class="tabla"><table><thead><tr><th>Categoría</th><th>Facturación anual máxima</th>'
            '<th>Cuota mensual servicios</th><th>Cuota mensual venta de cosas</th></tr></thead>'
            f'<tbody>{filas}</tbody></table></div>'
            f'<p class="nota">Fuente: ARCA, {VIGENCIA}. La cuota incluye impuesto integrado, aporte jubilatorio (SIPA) y obra social.</p>')


def tabla_parametros():
    filas = ''.join(f'<tr><td><strong>{c[0]}</strong></td><td>${c[1]}</td><td>Hasta {c[2]}</td><td>Hasta {c[3]}</td><td>${c[4]}</td></tr>' for c in CATEGORIAS)
    return ('<div class="tabla"><table><thead><tr><th>Cat.</th><th>Ingresos brutos anuales</th><th>Superficie</th>'
            f'<th>Energía anual</th><th>Alquileres anuales</th></tr></thead><tbody>{filas}</tbody></table></div>'
            f'<p class="nota">Fuente: ARCA, {VIGENCIA}. La superficie no se considera en localidades de menos de 40.000 habitantes (salvo excepciones).</p>')


def tabla_componentes():
    filas = ''.join(f'<tr><td><strong>{c[0]}</strong></td><td>${c[5]}</td><td>${c[6]}</td><td>${c[7]}</td><td>${c[8]}</td></tr>' for c in CATEGORIAS)
    return ('<div class="tabla"><table><thead><tr><th>Cat.</th><th>Impuesto integrado (servicios)</th>'
            '<th>Impuesto integrado (venta)</th><th>Jubilación (SIPA)</th><th>Obra social</th></tr></thead>'
            f'<tbody>{filas}</tbody></table></div><p class="nota">Fuente: ARCA, {VIGENCIA}. Importes mensuales.</p>')


GUIAS = [
    {
        'slug': 'categorias-monotributo',
        'corto': 'Categorías del monotributo',
        'titulo': 'Categorías del Monotributo 2026: topes y cuotas | AltaMonotributo',
        'descripcion': 'Tabla de categorías del monotributo de la A a la K con los topes de facturación y las cuotas vigentes desde agosto de 2026. Qué define tu categoría y cómo elegir la correcta.',
        'h1': 'Categorías del monotributo 2026: topes de facturación y cuotas',
        'bajada': 'La tabla completa de la A a la K con los valores vigentes desde agosto de 2026, y cómo saber en qué categoría te corresponde estar.',
        'respuesta': '<strong>El monotributo tiene 11 categorías, de la A a la K.</strong> Tu categoría depende principalmente de cuánto facturás en los últimos 12 meses: con los '
                     'valores vigentes desde agosto de 2026, la categoría A llega hasta <strong>$12.009.410,45</strong> anuales y la K hasta <strong>$126.610.838,75</strong>. '
                     'También cuentan la superficie del local, la energía que consumís y el alquiler que pagás: quedás en la categoría más alta que te marque cualquiera de esos parámetros.',
        'cuerpo': f"""<h2>Tabla de categorías y cuotas 2026</h2>
<p>Estos son los topes de facturación anual y la cuota mensual que pagás en cada categoría:</p>
{tabla_topes()}
<h2>¿Qué define tu categoría?</h2>
<p>ARCA mira cuatro parámetros. Te corresponde la categoría más alta que resulte de cualquiera de ellos:</p>
<ol>
<li><strong>Ingresos brutos de los últimos 12 meses</strong>: es el parámetro principal. Se cuenta lo que facturaste por tu actividad independiente.</li>
<li><strong>Superficie afectada a la actividad</strong>: si tenés local, oficina o depósito.</li>
<li><strong>Energía eléctrica consumida</strong> en el año en ese lugar.</li>
<li><strong>Alquileres devengados</strong> en el año por ese lugar.</li>
</ol>
{tabla_parametros()}
<h2>Cómo elegir la categoría correcta</h2>
<p>Si recién empezás, la categoría se define con lo que estimás facturar en los próximos 12 meses. Elegir una categoría más baja de la que corresponde puede generar diferencias, intereses y una recategorización de oficio por parte de ARCA; elegir una más alta te hace pagar de más todos los meses.</p>
<p>Después del alta, la categoría se revisa dos veces por año en la <a href="/guias/recategorizacion-monotributo">recategorización</a>. Si superás el tope de la categoría K, quedás excluido del monotributo y pasás al régimen general.</p>
<h2>Servicios o venta de cosas muebles</h2>
<p>Desde la categoría C, la cuota es distinta según si prestás servicios o vendés productos: el componente impositivo es más alto para servicios. Si hacés las dos cosas, consultá con un contador cuál te corresponde.</p>""",
        'faq': [
            ('¿Cuál es el tope de la categoría A en 2026?', 'Con los valores vigentes desde el 1 de agosto de 2026, el tope de ingresos brutos anuales de la categoría A es de $12.009.410,45.'),
            ('¿Cuántas categorías tiene el monotributo?', 'Once, de la A a la K. La A es la de menor facturación y cuota; la K, la más alta.'),
            ('¿Qué pasa si facturo más que el tope de la categoría K?', 'Quedás excluido del monotributo y tenés que pasar al régimen general (IVA y Ganancias). Antes de llegar a ese punto conviene revisarlo con un contador.'),
            ('¿Cada cuánto se actualizan los valores?', 'Los montos se actualizan dos veces por año. La tabla de esta guía corresponde a los valores vigentes desde agosto de 2026.'),
        ],
        'cta_titulo': '¿No sabés qué categoría te toca?',
        'cta_texto': 'Hacemos tu alta y elegimos la categoría correcta según tu actividad e ingresos. Constancia oficial en menos de 24 hs hábiles.',
        'wa': 'Hola, quiero saber qué categoría de monotributo me corresponde',
        'fuentes': [ARCA_CATEGORIAS],
    },
    {
        'slug': 'cuanto-se-paga-monotributo',
        'corto': 'Cuánto se paga de monotributo',
        'titulo': '¿Cuánto se paga de monotributo en 2026? | AltaMonotributo',
        'descripcion': 'Cuánto se paga de monotributo por mes en 2026: cuota de cada categoría desde $49.527,18, qué incluye (impuesto, jubilación y obra social), cuándo vence y cómo pagarlo.',
        'h1': '¿Cuánto se paga de monotributo en 2026?',
        'bajada': 'La cuota mensual de cada categoría, qué estás pagando en cada componente y cuándo vence.',
        'respuesta': '<strong>Con los valores vigentes desde agosto de 2026, la cuota mensual del monotributo va de $49.527,18 (categoría A) a $1.614.446,04 (categoría K, servicios).</strong> '
                     'La cuota incluye tres cosas: el impuesto integrado, el aporte jubilatorio (SIPA) y la obra social. Se paga todos los meses y vence el día 20.',
        'cuerpo': f"""<h2>Cuota mensual por categoría</h2>
{tabla_topes()}
<h2>Qué incluye la cuota</h2>
<p>La cuota del monotributo reemplaza varios impuestos y aportes que de otra forma pagarías por separado:</p>
<ul>
<li><strong>Impuesto integrado</strong>: reemplaza al IVA y a Ganancias por tu actividad.</li>
<li><strong>Aporte jubilatorio (SIPA)</strong>: cada mes pago suma para tu jubilación.</li>
<li><strong>Obra social</strong>: te da cobertura médica (y podés sumar a tu grupo familiar pagando un adicional).</li>
</ul>
{tabla_componentes()}
<h2>Casos en los que pagás menos</h2>
<p>Si además trabajás <a href="/guias/monotributo-y-relacion-de-dependencia">en relación de dependencia</a>, tu empleador ya hace los aportes de jubilación y obra social, así que en el monotributo no elegís obra social. Los jubilados tampoco pagan el componente de obra social. Cada caso tiene sus reglas: conviene revisarlo con un contador antes de inscribirte.</p>
<h2>Cuándo vence y cómo se paga</h2>
<p>La cuota vence el <strong>20 de cada mes</strong>. Se puede pagar con un VEP desde home banking, con débito automático en cuenta o tarjeta, o con los medios de pago habilitados por ARCA. Si no la pagás a tiempo se generan intereses: mirá <a href="/guias/que-pasa-si-no-pago-monotributo">qué pasa si no pagás el monotributo</a>.</p>""",
        'faq': [
            ('¿Cuánto se paga de monotributo en la categoría A?', 'Con los valores vigentes desde agosto de 2026, la cuota mensual de la categoría A es de $49.527,18, tanto para servicios como para venta de cosas muebles.'),
            ('¿Cuándo vence el monotributo?', 'La cuota vence el día 20 de cada mes.'),
            ('¿La cuota del monotributo incluye obra social?', 'Sí. La cuota incluye el impuesto integrado, el aporte jubilatorio y la obra social. Si trabajás en relación de dependencia, la obra social te la da tu empleador.'),
            ('¿El precio del alta incluye la cuota mensual?', 'No. La cuota mensual se paga directamente a ARCA. El servicio de alta de AltaMonotributo es un honorario único por hacer el trámite por vos.'),
        ],
        'cta_titulo': 'Empezá a facturar este mes',
        'cta_texto': 'Hacemos tu alta en el monotributo con la categoría correcta para que no pagues de más. Menos de 24 hs hábiles.',
        'wa': 'Hola, quiero saber cuánto voy a pagar de monotributo',
        'fuentes': [ARCA_CATEGORIAS],
    },
    {
        'slug': 'factura-c-monotributo',
        'corto': 'Cómo hacer una factura C',
        'titulo': 'Cómo hacer una factura C: paso a paso (2026) | AltaMonotributo',
        'descripcion': 'Guía paso a paso para hacer una factura C en ARCA: punto de venta, Comprobantes en línea y la app Facturador. Qué necesitás y errores comunes.',
        'h1': 'Cómo hacer una factura C como monotributista, paso a paso',
        'bajada': 'Qué necesitás, cómo dar de alta el punto de venta y cómo emitir la factura en ARCA o desde el celular.',
        'respuesta': '<strong>Los monotributistas emiten factura C.</strong> Para hacerla necesitás tu CUIT, Clave Fiscal nivel 3 y un punto de venta habilitado. '
                     'Se emite gratis desde el servicio <strong>Comprobantes en línea</strong> de ARCA, o desde la app <strong>Facturador</strong> en el celular.',
        'cuerpo': """<h2>Qué necesitás antes de facturar</h2>
<ul>
<li>Estar inscripto en el monotributo (si todavía no lo estás, <a href="/#formulario">te damos de alta</a>).</li>
<li>CUIT y Clave Fiscal nivel 3 o superior.</li>
<li>Los servicios <em>Comprobantes en línea</em> y <em>Administración de puntos de venta y domicilios</em> habilitados en tu Clave Fiscal.</li>
</ul>
<h2>Paso 1: dar de alta el punto de venta</h2>
<p>Si no tenés un punto de venta, ARCA puede crearlo de oficio en Comprobantes en línea con la opción "Factura en línea - Monotributo", asociado a tu domicilio fiscal. Para hacerlo vos, entrá al servicio <strong>Administración de puntos de venta y domicilios</strong>, elegí la opción de alta, cargá un número (por ejemplo 0002) y seleccioná "Factura en línea - Monotributo".</p>
<h2>Paso 2: configurar tus datos</h2>
<p>Entrá a <strong>Comprobantes en línea</strong>, elegí tu nombre y completá los <em>Datos adicionales del comprobante</em> (por ejemplo, la condición frente al IVA y el domicilio comercial). Se hace una sola vez.</p>
<h2>Paso 3: generar la factura C</h2>
<ol>
<li>En Comprobantes en línea, elegí <strong>Generar comprobantes</strong>, tu punto de venta y el tipo <strong>Factura C</strong>.</li>
<li>Completá la fecha y el concepto: productos, servicios o ambos. Si son servicios, indicá el período facturado y el vencimiento del pago.</li>
<li>Cargá los datos del receptor: si es consumidor final podés no identificarlo (según el monto); si es una empresa, su CUIT y su condición frente al IVA.</li>
<li>Agregá el detalle (descripción, cantidad y precio) y confirmá. ARCA asigna un CAE y la factura queda emitida.</li>
<li>Descargá el PDF para mandarlo. Siempre podés volver a buscarla en la opción de consultas.</li>
</ol>
<h2>Facturar desde el celular</h2>
<p>ARCA tiene la app <strong>Facturador</strong>, para emitir tiques y notas de crédito C a consumidores finales desde el celular o la computadora, si cumplís los requisitos. Si no, usás Comprobantes en línea desde el navegador del celular.</p>
<h2>Errores comunes</h2>
<ul>
<li><strong>Facturar más que el tope de tu categoría</strong>: antes de emitir, revisá cuánto llevás facturado en los últimos 12 meses (mirá las <a href="/guias/categorias-monotributo">categorías</a>).</li>
<li><strong>Equivocarse en el tipo de comprobante o en el receptor</strong>: no se borra, se corrige con una nota de crédito C.</li>
<li><strong>Olvidarse del período en servicios</strong>: las fechas del servicio son obligatorias.</li>
</ul>""",
        'faq': [
            ('¿Qué tipo de factura hace un monotributista?', 'Factura C. Las facturas A y B son para responsables inscriptos en IVA.'),
            ('¿Tiene costo hacer una factura en ARCA?', 'No. Emitir comprobantes desde Comprobantes en línea o desde el Facturador de ARCA es gratuito.'),
            ('¿Cómo anulo una factura C mal hecha?', 'Las facturas electrónicas no se anulan: se emite una nota de crédito C por el mismo importe que la factura equivocada.'),
            ('¿Puedo facturar sin estar inscripto en el monotributo?', 'No. Para emitir facturas a tu nombre tenés que estar inscripto en algún régimen; el monotributo es el más simple para empezar.'),
        ],
        'cta_titulo': '¿Todavía no podés facturar?',
        'cta_texto': 'Te damos de alta en el monotributo y te dejamos listo para emitir tu primera factura C. Menos de 24 hs hábiles.',
        'wa': 'Hola, quiero darme de alta para poder facturar',
        'fuentes': [('ARCA — Facturación del monotributo', 'https://www.afip.gob.ar/monotributo/ayuda/facturacion.asp'),
                    ('Argentina.gob.ar — Emitir factura electrónica', 'https://www.argentina.gob.ar/emitir-factura-electronica-para-monotributistas'),
                    ('ARCA — Facturador', 'https://www.arca.gob.ar/facturador/caracteristicas-y-funciones/que-es.asp')],
    },
    {
        'slug': 'monotributo-y-relacion-de-dependencia',
        'corto': 'Monotributo y relación de dependencia',
        'titulo': 'Monotributo y relación de dependencia: ¿se puede? | AltaMonotributo',
        'descripcion': 'Sí, podés ser monotributista y empleado a la vez. Qué pagás, qué declarás al inscribirte, por qué no elegís obra social y qué ingresos cuentan para la categoría.',
        'h1': '¿Puedo tener monotributo y trabajar en relación de dependencia?',
        'bajada': 'Sí, y es muy común. Te explicamos qué pagás, qué tenés que declarar y qué ingresos cuentan para tu categoría.',
        'respuesta': '<strong>Sí, podés.</strong> Ser monotributista por una actividad independiente es compatible con tener un empleo en relación de dependencia. '
                     'Al inscribirte declarás el CUIT de tu empleador y la fecha de inicio del empleo, y <strong>no elegís obra social</strong> en el monotributo porque te la da tu empleador. '
                     'Tu sueldo no cuenta para la categoría: solo cuenta lo que facturás por tu actividad independiente.',
        'cuerpo': """<h2>Qué pagás si sos empleado y monotributista</h2>
<p>Tu empleador ya hace los aportes de jubilación y obra social por tu sueldo. Por eso, según el caso, en el monotributo no pagás de nuevo esos componentes: la obra social no la elegís en el monotributo, y el aporte jubilatorio depende de si el monotributo es tu única fuente de ingresos o si también trabajás en relación de dependencia. El impuesto integrado se paga siempre.</p>
<h2>Qué declarás al inscribirte</h2>
<p>En el alta elegís la opción de trabajador en relación de dependencia e informás:</p>
<ul>
<li>El <strong>CUIT de tu empleador</strong>.</li>
<li>La <strong>fecha en que empezaste</strong> a trabajar.</li>
</ul>
<p>Si cambiás de trabajo o dejás de ser empleado, hay que actualizarlo, porque cambia lo que pagás.</p>
<h2>Qué ingresos cuentan para la categoría</h2>
<p>La <a href="/guias/categorias-monotributo">categoría</a> se calcula solo con lo que facturás por tu actividad independiente. El sueldo no se suma.</p>
<h2>Casos para revisar con un contador</h2>
<ul>
<li>Si facturás servicios a la misma empresa que te paga el sueldo.</li>
<li>Si querés inscribirte en el monotributo social o promovido: tienen requisitos distintos.</li>
<li>Si tenés más de un empleo o trabajás en el exterior.</li>
</ul>""",
        'faq': [
            ('¿Pago obra social dos veces si soy empleado y monotributista?', 'No. Si trabajás en relación de dependencia, la obra social te la da tu empleador y en el monotributo no elegís una.'),
            ('¿Mi sueldo cuenta para el tope del monotributo?', 'No. Para la categoría solo cuentan los ingresos de tu actividad independiente.'),
            ('¿Qué datos del empleo tengo que informar?', 'El CUIT de tu empleador y la fecha en que empezaste a trabajar.'),
        ],
        'cta_titulo': 'Te damos de alta aunque tengas un empleo',
        'cta_texto': 'Nos encargamos del alta, elegimos tu categoría y configuramos bien los aportes para que no pagues de más.',
        'wa': 'Hola, trabajo en relación de dependencia y quiero darme de alta en el monotributo',
        'fuentes': [('ARCA — Jubilación y obra social', 'https://www.afip.gob.ar/monotributo/ayuda/jubilacion.asp')],
    },
    {
        'slug': 'recategorizacion-monotributo',
        'corto': 'Recategorización',
        'titulo': 'Recategorización del monotributo 2026: cuándo y cómo | AltaMonotributo',
        'descripcion': 'Qué es la recategorización del monotributo, cuándo se hace (febrero y agosto), quién está obligado, cómo calcular tu categoría y qué pasa si no te recategorizás.',
        'h1': 'Recategorización del monotributo: cuándo es y cómo hacerla',
        'bajada': 'Dos veces por año tenés que revisar si tu categoría sigue siendo la correcta. Te contamos cuándo, cómo y qué pasa si no lo hacés.',
        'respuesta': '<strong>La recategorización es la revisión semestral de tu categoría.</strong> En 2026 se hizo en dos ventanas: hasta el <strong>5 de febrero</strong> y hasta el <strong>5 de agosto</strong>. '
                     'Se calcula con tus ingresos, superficie, energía y alquileres de los últimos 12 meses. Si tus parámetros te cambian de categoría, tenés que recategorizarte; si no, ARCA puede hacerlo de oficio.',
        'cuerpo': """<h2>Cuándo se hace</h2>
<p>La recategorización es dos veces por año. En 2026, el plazo venció el <strong>5 de febrero</strong> y el <strong>5 de agosto</strong>; después de cada ventana, ARCA puede recategorizar de oficio a quienes no lo hicieron. La próxima ventana corresponde a principios de 2027: confirmá la fecha exacta en ARCA cuando se publique.</p>
<h2>Quién tiene que recategorizarse</h2>
<ul>
<li>Quienes, con los últimos 12 meses, quedan en una categoría distinta de la que tienen.</li>
<li>No tienen que hacerlo quienes llevan menos de seis meses en el régimen, ni quienes siguen dentro de los parámetros de su categoría actual.</li>
</ul>
<h2>Cómo calcular tu nueva categoría</h2>
<ol>
<li>Sumá lo que facturaste en los últimos 12 meses.</li>
<li>Revisá superficie, energía y alquileres si tenés local.</li>
<li>Buscá en la <a href="/guias/categorias-monotributo">tabla de categorías</a> la categoría más alta que te marque cualquiera de esos parámetros.</li>
<li>Si cambia, hacé el trámite en el Portal Monotributo con tu Clave Fiscal, dentro del plazo.</li>
</ol>
<h2>Qué pasa si no te recategorizás</h2>
<p>Si te correspondía subir y no lo hiciste, ARCA puede recategorizarte de oficio, cobrarte la diferencia con intereses y aplicar sanciones. Si te correspondía bajar y no lo hiciste, simplemente seguís pagando de más hasta la próxima ventana. Y si superaste el tope de la categoría más alta, ya no es una recategorización: es una exclusión del régimen.</p>""",
        'faq': [
            ('¿Cuándo es la recategorización del monotributo?', 'Dos veces por año. En 2026 los plazos vencieron el 5 de febrero y el 5 de agosto. La próxima es a principios de 2027.'),
            ('¿Qué período se toma para recategorizarme?', 'Los últimos 12 meses anteriores a la recategorización: ingresos, superficie, energía y alquileres.'),
            ('¿Tengo que recategorizarme si sigo en la misma categoría?', 'No. Solo si tus parámetros te llevan a una categoría distinta.'),
            ('¿Qué pasa si no me recategorizo?', 'ARCA puede recategorizarte de oficio, cobrarte la diferencia con intereses y aplicar sanciones.'),
        ],
        'cta_titulo': '¿Querés que te recategoricemos?',
        'cta_texto': 'El equipo de Tributo Simple revisa tus ingresos, te dice qué categoría te toca y hace el trámite por vos.',
        'wa': 'Hola, quiero ayuda con la recategorización del monotributo',
        'fuentes': [ARCA_CATEGORIAS, ('ARCA — Ayuda del monotributo', 'https://www.arca.gob.ar/monotributo/ayuda/tutoriales.asp')],
    },
    {
        'slug': 'que-pasa-si-no-pago-monotributo',
        'corto': 'Qué pasa si no pago el monotributo',
        'titulo': '¿Qué pasa si no pago el monotributo? | AltaMonotributo',
        'descripcion': 'Qué pasa si dejás de pagar el monotributo: intereses, baja de oficio después de 10 meses sin pagar, cómo regularizar la deuda y cómo volver a inscribirte.',
        'h1': '¿Qué pasa si no pago el monotributo?',
        'bajada': 'Intereses, deuda y baja de oficio: qué pasa si dejás de pagar y cómo regularizarlo.',
        'respuesta': '<strong>Si no pagás el monotributo, la deuda genera intereses todos los meses.</strong> Si dejás de pagar <strong>10 meses seguidos</strong>, ARCA puede darte de baja de oficio, sin aviso previo. '
                     'Para volver tenés que regularizar la deuda (pagarla o entrar en un plan de pagos) y recién ahí inscribirte de nuevo.',
        'cuerpo': """<h2>Intereses desde el día siguiente al vencimiento</h2>
<p>La cuota vence el 20 de cada mes. Si no la pagás, la deuda empieza a generar intereses y sigue acumulándose mes a mes. Además, tener deuda puede trabar otros trámites, como recategorizarte o acceder a algunos planes de pago.</p>
<h2>Baja de oficio por falta de pago</h2>
<p>Si no pagás durante <strong>10 meses consecutivos</strong>, ARCA puede darte de baja del monotributo automáticamente, sin notificación previa. La deuda no desaparece con la baja: sigue a tu nombre.</p>
<h2>Cómo regularizar la deuda</h2>
<ol>
<li>Revisá cuánto debés en tu cuenta corriente de monotributo en ARCA (con Clave Fiscal).</li>
<li>Pagala con VEP desde home banking o, si no te alcanza, adherí a un <strong>plan de facilidades de pago</strong>.</li>
<li>Si te habían dado de baja, una vez cancelada la deuda o incluida en un plan, podés volver a inscribirte. El reingreso no es automático.</li>
</ol>
<h2>Si querés dejar la actividad</h2>
<p>No dejes de pagar para "darte de baja": pedí la <strong>baja por cese de actividad</strong>. El mes en que pedís la baja tiene que quedar pago. Así no se acumula deuda a tu nombre.</p>""",
        'faq': [
            ('¿Cuántos meses sin pagar el monotributo te dan de baja?', 'Si no pagás 10 meses consecutivos, ARCA puede darte de baja de oficio.'),
            ('¿La deuda desaparece si me dan de baja?', 'No. La deuda sigue a tu nombre y para volver al monotributo tenés que regularizarla.'),
            ('¿Puedo pagar la deuda del monotributo en cuotas?', 'Sí, ARCA tiene planes de facilidades de pago. Las condiciones dependen del plan vigente y de tu situación.'),
            ('¿Cómo vuelvo al monotributo después de una baja por deuda?', 'Primero cancelás la deuda o la incluís en un plan de pagos; después hacés una nueva inscripción. Nosotros podemos hacer la reinscripción por vos.'),
        ],
        'cta_titulo': '¿Te dieron de baja? Te reinscribimos',
        'cta_texto': 'Revisamos tu situación y hacemos la reinscripción en el monotributo. Si tenés deuda, te orientamos para regularizarla.',
        'wa': 'Hola, tengo deuda de monotributo y quiero regularizar mi situación',
        'fuentes': [('ARCA — Baja de oficio', 'https://arca.gob.ar/monotributo/ayuda/de-oficio.asp'),
                    ('Argentina.gob.ar — Darme de baja en el monotributo', 'https://www.argentina.gob.ar/servicio/darme-de-baja-en-el-monotributo')],
    },
]
