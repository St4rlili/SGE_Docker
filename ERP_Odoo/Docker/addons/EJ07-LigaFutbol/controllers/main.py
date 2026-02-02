# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

#Clase del controlador web
class Main(http.Controller):
    #Decorador que indica que la url "/ligafutbol/equipo/json" atendera por HTTP, sin autentificacion
    #Devolvera texto que estará en formato JSON
    #Se puede probar accediendo a http://localhost:8069/ligafutbol/equipo/json
    @http.route('/ligafutbol/equipo/json', type='http', auth='none')
    def obtenerDatosEquiposJSON(self):
        #Obtenemos la referencia al modelo de Equipo
        equipos = request.env['liga.equipo'].sudo().search([])
        
        #Generamos una lista con informacion que queremos sacar en JSON
        listaDatosEquipos=[]
        for equipo in equipos:
             listaDatosEquipos.append([equipo.nombre,str(equipo.fecha_fundacion),equipo.jugados,equipo.puntos,equipo.victorias,equipo.empates,equipo.derrotas])
        #Convertimos la lista generada a JSON
        json_result=json.dumps(listaDatosEquipos)

        return json_result
    
    @http.route('/eliminarempates', type='http', auth='none')
    def eliminar_empates(self):
        # Buscamos todos los partidos que hayan terminado en empate
        partidos_empate = request.env['liga.partido'].sudo().search([]).filtered(
            lambda p: p.goles_casa == p.goles_fuera
        )


        # Contamos cuántos hay antes de eliminar
        total_eliminados = len(partidos_empate)

        # Eliminamos los partidos encontrados
        partidos_empate.unlink()

        # Devolvemos el número de partidos eliminados como texto
        return f"Se han eliminado {total_eliminados} partidos en empate."