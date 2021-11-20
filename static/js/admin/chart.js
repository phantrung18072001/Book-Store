$(function() {
  /* ChartJS
   * -------
   * Data and config for chartjs
   */
  'use strict';
  var data = {
    labels: ["", "", "", "", ""],
    datasets: [{
      label: 'Doanh thu',
      data: [1, 1, 1, 1, 1],
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)'
      ],
      borderColor: [
        'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
      ],
      borderWidth: 1,
      fill: false
    }]
  }

  var PieData = {
    labels: ["", "", "", "", ""],
    datasets: [{
      data: [1, 1, 1, 1],
      backgroundColor: [
        'rgba(255, 99, 132, 0.5)',
        'rgba(54, 162, 235, 0.5)',
        'rgba(255, 206, 86, 0.5)',
        'rgba(75, 192, 192, 0.5)',
        'rgba(153, 102, 255, 0.5)',
        'rgba(255, 159, 64, 0.5)'
      ],
      borderColor: [
        'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
      ],
    }],
  };
  var options = {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    },
    legend: {
      display: false
    },
    elements: {
      point: {
        radius: 0
      }
    }
  };
  
  var month1 = "Tháng " + $("#month1").text();
  var month2 = "Tháng " + $("#month2").text();
  var month3 = "Tháng " + $("#month3").text();
  var month4 = "Tháng " + $("#month4").text();
  var month5 = "Tháng " + $("#month5").text();
  data.labels = [month1, month2, month3, month4, month5];

  var revenueByMonth1 = Number($("#revenueByMonth1").text());
  var revenueByMonth2 = Number($("#revenueByMonth2").text());
  var revenueByMonth3 = Number($("#revenueByMonth3").text());
  var revenueByMonth4 = Number($("#revenueByMonth4").text());
  var revenueByMonth5 = Number($("#revenueByMonth5").text());
  data.datasets[0].data = [revenueByMonth1, revenueByMonth2, revenueByMonth3, revenueByMonth4, revenueByMonth5];

  // Get context with jQuery - using jQuery's .get() method.
  if ($("#revenueByMonth").length) {
    var barChartCanvas = $("#revenueByMonth").get(0).getContext("2d");
    // This will get the first returned node in the jQuery collection.
    var barChart = new Chart(barChartCanvas, {
      type: 'bar',
      data: data,
      options: options
    });
  }

  var Bestsellers1 = $("#Bestsellers1").text();
  var Bestsellers2 = $("#Bestsellers2").text();
  var Bestsellers3 = $("#Bestsellers3").text();
  var Bestsellers4 = $("#Bestsellers4").text();
  var total_books_sold = $("#total_books_sold").text();
  var Bestsellers1_quantity = (Number($("#Bestsellers1_quantity").text()) / total_books_sold * 100).toFixed(2);
  var Bestsellers2_quantity = (Number($("#Bestsellers2_quantity").text()) / total_books_sold * 100).toFixed(2);
  var Bestsellers3_quantity = (Number($("#Bestsellers3_quantity").text()) / total_books_sold * 100).toFixed(2);
  var Bestsellers4_quantity = 100 - Bestsellers1_quantity - Bestsellers2_quantity - Bestsellers3_quantity;
  PieData.labels = [Bestsellers1, Bestsellers2, Bestsellers3, Bestsellers4];
  PieData.datasets[0].data = [Bestsellers1_quantity, Bestsellers2_quantity, Bestsellers3_quantity, Bestsellers4_quantity ];

  var PieOptions = {
    responsive: true,
    animation: {
      animateScale: true,
      animateRotate: true
    }
  };

  if ($("#bestsellers").length) {
    var pieChartCanvas = $("#bestsellers").get(0).getContext("2d");
    var pieChart = new Chart(pieChartCanvas, {
      type: 'pie',
      data: PieData,
      options: PieOptions
    });
  }
});