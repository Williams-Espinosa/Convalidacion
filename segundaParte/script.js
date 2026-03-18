require('dotenv').config();

const API_KEY = process.env.API_KEY;
const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_KEY = process.env.SUPABASE_KEY;

let dinero = 10000;
let portafolio = {};
let precioActual = 0;
let simboloActual = "";
let chart = null;

function log(m) {
const div = document.getElementById("log");
const e = document.createElement("div");
e.textContent = new Date().toLocaleTimeString() + " " + m;
div.prepend(e);
}

function actualizarSaldo() {
document.getElementById("saldo").textContent = dinero.toFixed(2);
}

function actualizarStats() {

let valor = 0;

for (let s in portafolio) {
valor += portafolio[s].cantidad * portafolio[s].precioActual;
}

document.getElementById("valor").textContent = valor.toFixed(2);

let roi = ((dinero + valor - 10000) / 10000) * 100;
document.getElementById("roi").textContent = roi.toFixed(2) + "%";

}

async function buscar() {

try {

const symbol = document.getElementById("symbol").value.toUpperCase();

const url = `https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${symbol}&apikey=${API_KEY}`;

const res = await fetch(url);
const data = await res.json();

if (!data["Global Quote"]) {
alert("Símbolo no encontrado");
return;
}

const precio = parseFloat(data["Global Quote"]["05. price"]);

precioActual = precio;
simboloActual = symbol;

document.getElementById("precio").textContent = "Precio: $" + precio.toFixed(2);

document.getElementById("comprarBtn").disabled = false;
document.getElementById("venderBtn").disabled = false;

graficarPrecio(precio);

log("Precio actualizado " + symbol);

} catch (e) {

alert("Error obteniendo datos");

}

}

function comprar() {

const cantidad = parseInt(document.getElementById("cantidad").value);

if (!cantidad || cantidad <= 0) {
alert("Cantidad inválida");
return;
}

const costo = precioActual * cantidad;

if (costo > dinero) {
alert("Fondos insuficientes");
return;
}

dinero -= costo;

if (!portafolio[simboloActual]) {

portafolio[simboloActual] = {
cantidad: 0,
precioCompra: precioActual,
precioActual: precioActual
};

}

portafolio[simboloActual].cantidad += cantidad;
portafolio[simboloActual].precioActual = precioActual;

guardarOperacion("compra", simboloActual, cantidad, precioActual);

renderPortafolio();
actualizarSaldo();
actualizarStats();

log("Compra " + simboloActual);

}

function vender() {

const cantidad = parseInt(document.getElementById("cantidad").value);

if (!portafolio[simboloActual]) {
alert("No tienes este activo");
return;
}

if (cantidad > portafolio[simboloActual].cantidad) {
alert("No tienes suficientes acciones");
return;
}

dinero += precioActual * cantidad;

portafolio[simboloActual].cantidad -= cantidad;
portafolio[simboloActual].precioActual = precioActual;

if (portafolio[simboloActual].cantidad === 0) {
delete portafolio[simboloActual];
}

guardarOperacion("venta", simboloActual, cantidad, precioActual);

renderPortafolio();
actualizarSaldo();
actualizarStats();

log("Venta " + simboloActual);

}

function renderPortafolio() {

const tbody = document.getElementById("tablaPortafolio");

const keys = Object.keys(portafolio);

if (keys.length === 0) {
tbody.innerHTML = "<tr><td colspan='5'>Sin activos</td></tr>";
return;
}

tbody.innerHTML = keys.map(s => {

let p = portafolio[s];

let roi = ((p.precioActual - p.precioCompra) / p.precioCompra) * 100;

return `
<tr>
<td>${s}</td>
<td>${p.cantidad}</td>
<td>$${p.precioCompra.toFixed(2)}</td>
<td>$${p.precioActual.toFixed(2)}</td>
<td>${roi.toFixed(2)}%</td>
</tr>
`;

}).join("");

}

function graficarPrecio(precio) {

const ctx = document.getElementById("grafica");

if (chart) chart.destroy();

chart = new Chart(ctx, {
type: "line",
data: {
labels: ["Precio"],
datasets: [{
label: "Precio actual",
data: [precio]
}]
}
});

}

function graficar(datos, titulo) {

const ctx = document.getElementById("grafica");

if (chart) chart.destroy();

chart = new Chart(ctx, {
type: "line",
data: {
labels: datos.map((_, i) => i),
datasets: [{
label: titulo,
data: datos
}]
}
});

}

function simulacionMonteCarlo() {

let capital = 1000;
let datos = [capital];

for (let i = 0; i < 30; i++) {

let r = Math.random() * 0.2 - 0.05;
capital = capital * (1 + r);

datos.push(capital);

}

graficar(datos, "Monte Carlo");

log("Simulación Monte Carlo ejecutada");

}

function simularPortafolio() {

let capital = 1000;
let datos = [capital];

for (let i = 0; i < 50; i++) {

let r = Math.random() * 0.1;
capital = capital * (1 + r);

datos.push(capital);

}

graficar(datos, "Simulación Portafolio");

log("Simulación portafolio ejecutada");

}

function estrategiaBuyHold() {

let futuro = precioActual * (1 + (Math.random() * 0.3));

alert("Valor futuro estimado: $" + futuro.toFixed(2));

}

function estrategiaMomentum() {

let momentum = precioActual * (1 + (Math.random() * 0.1));

alert("Predicción Momentum: $" + momentum.toFixed(2));

}

function analizarRiesgo() {

let precios = [];

for (let s in portafolio) {
precios.push(portafolio[s].precioActual);
}

if (precios.length === 0) {
alert("Portafolio vacío");
return;
}

let media = precios.reduce((a, b) => a + b) / precios.length;

let varianza = precios.reduce((s, x) => s + (x - media) ** 2, 0) / precios.length;

let desv = Math.sqrt(varianza);

alert("Volatilidad estimada: " + desv.toFixed(2));

}

function prediccionIA() {

let pred = precioActual * (1 + (Math.random() * 0.15 - 0.05));

alert("Predicción IA precio: $" + pred.toFixed(2));

}

async function guardarOperacion(tipo, simbolo, cantidad, precio) {

try {

await fetch(SUPABASE_URL, {
method: "POST",
headers: {
"apikey": SUPABASE_KEY,
"Authorization": "Bearer " + SUPABASE_KEY
},
body: JSON.stringify({
tipo,
simbolo,
cantidad,
precio
})
});

cargarOperaciones();

} catch (e) {

console.error("Error guardando operación");

}

}

async function cargarOperaciones() {

try {

const res = await fetch(SUPABASE_URL + "?select=*&order=fecha.desc", {
method: "GET",
headers: {
"apikey": SUPABASE_KEY,
"Authorization": "Bearer " + SUPABASE_KEY,
"Content-Type": "application/json"
}
});

const data = await res.json();

const tbody = document.getElementById("historial");

if (!data || data.length === 0) {
tbody.innerHTML = "<tr><td colspan='5'>Sin historial</td></tr>";
return;
}

tbody.innerHTML = data.map(o => `
<tr>
<td>${o.tipo}</td>
<td>${o.simbolo}</td>
<td>${o.cantidad}</td>
<td>$${o.precio ?? "-"}</td>
<td>${o.fecha ? new Date(o.fecha).toLocaleString() : "-"}</td>
</tr>
`).join("");

} catch (e) {

console.error("Error cargando historial", e);

}

}

window.onload = () => {

actualizarSaldo();
actualizarStats();
cargarOperaciones();

};