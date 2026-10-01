(function () {
  var goatCounterEndpoint = "https://idefcyt.goatcounter.com/count";
  var goatCounterScript = document.createElement("script");

  goatCounterScript.setAttribute("async", "true");
  goatCounterScript.setAttribute("src", "https://gc.zgo.at/count.js");
  goatCounterScript.setAttribute("data-goatcounter", goatCounterEndpoint);
  document.head.appendChild(goatCounterScript);

  var counterValue = document.querySelector("[data-visitor-count]");

  if (!counterValue) {
    return;
  }

  var historicalBase = Number(counterValue.getAttribute("data-historical-base") || "0");
  var counterNote = document.querySelector("[data-visitor-note]");

  fetch("https://idefcyt.goatcounter.com/counter/TOTAL.json", { cache: "no-store" })
    .then(function (response) {
      if (!response.ok) {
        throw new Error("GoatCounter public counter is not available.");
      }

      return response.json();
    })
    .then(function (data) {
      var currentVisits = Number(String(data.count || "").replace(/[^\d]/g, ""));

      if (!Number.isFinite(currentVisits)) {
        return;
      }

      counterValue.textContent = (historicalBase + currentVisits).toLocaleString("en-US");

      if (counterNote) {
        counterNote.textContent = "Visitas acumuladas: registro historico mas nuevas visitas desde GoatCounter.";
      }
    })
    .catch(function () {
      if (counterNote) {
        counterNote.textContent = "Visitas historicas registradas; el contador se actualiza cuando GoatCounter publica el total.";
      }
    });
})();
