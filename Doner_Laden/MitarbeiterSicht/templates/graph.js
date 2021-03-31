<canvas id="myChart" class="w-100 h-50"></canvas>
<script>
var ctx = document.getElementById('myChart').getContext('2d');
      new Chart(ctx, {
      // The type of chart we want to create
      type: 'line',

      // The data for our dataset
      data: {
          labels: ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag'],
          datasets: [{
              label: "Pizza",
              borderColor: 'rgb(189, 60, 40)',
              data: [0, 5, 39, 12, 28, 32, 40]
          },
          {
              label: "Kebab",
              borderColor: 'rgb(189, 184, 40)',
              data: [30, 10, 15, 25, 50, 5, 45]
          },
          {
              label: "Getraenke",
              borderColor: 'rgb(40, 57, 189)',
              data: [2, 5, 10, 18, 40, 50, 20]
          }],
      },

      // Configuration options go here
      options: {}
});
</script>

