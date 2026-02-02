# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from PIL import Image
from io import BytesIO
import base64
import random

class GenerarImagenAleatoria(http.Controller):

    @http.route('/imagen/aleatoria', auth='public', cors='*', type='http')
    def crearImagen(self, ancho=200, alto=200, formato='html', **kw):
        # Convertimos parámetros a enteros
        try:
            ancho = int(ancho)
            alto = int(alto)
        except ValueError:
            return "Parámetros inválidos. Usa enteros para ancho y alto."

        # Creamos imagen RGB
        img = Image.new('RGB', (ancho, alto))

        # Generamos píxeles aleatorios
        pixels = [(random.randint(0,255), random.randint(0,255), random.randint(0,255))
                  for _ in range(ancho * alto)]
        img.putdata(pixels)

        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)

        if formato.lower() == 'png':
            # Devuelve la imagen directamente como PNG
            return request.make_response(
                buffer.getvalue(),
                headers=[('Content-Type', 'image/png')]
            )
        else:
            # Devuelve HTML con la imagen en Base64
            img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
            html = f'''
            <div>
                <h3>Imagen aleatoria {ancho}x{alto}</h3>
                <img src="data:image/png;base64,{img_str}"/>
            </div>
            '''
            return html
