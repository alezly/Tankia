<template>
    <div class="ghrap_container">
        <h2>visualización del llenado de agua</h2>
        <div id="container" style="width:100%; height:400px;"></div>

    </div>
</template>

<script>
import Highcharts from 'highcharts';

export default {
  name: "MainGraficas",
  data: function () {
    return {
      chart:null
    }
  },
  props: {
    valuesLitros: Array,
    valueTime: Number
  },
  methods: {
    init(){
      this.chart = Highcharts.chart('container', {
        title: {
            text: 'Historial de llenado',
            align: 'center'
        },


        yAxis: {
            title: {
                text: 'Velocidad de Litros por minuto'
            }
        },

        xAxis: {
            categories: [1.2,2.3,2.5,2.9,3,3.4],
            // accessibility: {
            //     rangeDescription: 'Range: 2010 to 2020'
            // }
        },

        legend: {
            layout: 'vertical',
            align: 'center',
            verticalAlign: 'bottom'
        },

        // plotOptions: {
        //     series: {
        //         label: {
        //             connectorAllowed: false
        //         },
        //         pointStart: 2010
        //     }
        // },

        series: [{
            name: 'Litros por minuto',
            data: [
                4,4.2,3.8,3.9,3.8,4,4.1,4
            ]
        }],

        // responsive: {
        //     rules: [{
        //         condition: {
        //             maxWidth: 500
        //         },
        //         chartOptions: {
        //             legend: {
        //                 layout: 'vertical',
        //                 align: 'center',
        //                 verticalAlign: 'bottom'
        //             }
        //         }
        //     }]
        // }

        });

    }
  },
  mounted(){
    this.init()

  }
};
</script>

<style>
.ghrap_container {
  width: 100%;
  height: 90%;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f3f4f6;
  border-radius: 1rem;
  margin: 0.5rem;
}
</style>
