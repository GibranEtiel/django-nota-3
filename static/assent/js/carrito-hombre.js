document.addEventListener('DOMContentLoaded', () => {
    const url = 'https://my.api.mockaroo.com/users.json?key=e4883c10';
    let carrito = [];

    fetch(url)
    .then(response => response.json())
    .then(data => {
        const zapatillasContainer = document.getElementById('zapatillas-container');
        const zapatillasHombre = data.filter(zapatilla => zapatilla.tipo === 'hombre');
        
        for (let i = 0; i < zapatillasHombre.length; i += 4) {
            const zapatillasGroup = zapatillasHombre.slice(i, i + 4);
            const row = document.createElement('div');
            row.classList.add('row', 'mt-4');

            zapatillasGroup.forEach(zapatilla => {
                const col = document.createElement('div');
                col.classList.add('col-md-3');

                const card = document.createElement('div');
                card.classList.add('card', 'mb-4', 'shadow-sm');
                card.setAttribute('data-toggle', 'modal');
                card.setAttribute('data-target', '#zapatillaModal');
                card.setAttribute('data-zapatilla-id', zapatilla.id);

                const img = document.createElement('img');
                img.classList.add('card-img-top');
                img.src = zapatilla.imagen;
                img.alt = zapatilla.nombre;

                const cardBody = document.createElement('div');
                cardBody.classList.add('card-body');

                const cardTitle = document.createElement('h5');
                cardTitle.classList.add('card-title');
                cardTitle.textContent = zapatilla.nombre;

                const cardText = document.createElement('p');
                cardText.classList.add('card-text');
                cardText.innerHTML = `<b><br>Tipo: ${zapatilla.tipo}<br><b>Precio:</b> $${zapatilla.precio}`;

                cardBody.appendChild(cardTitle);
                cardBody.appendChild(cardText);

                card.appendChild(img);
                card.appendChild(cardBody);

                col.appendChild(card);
                row.appendChild(col);
            });

            zapatillasContainer.appendChild(row);
        }

        document.querySelectorAll('.card').forEach(card => {
            card.addEventListener('click', () => {
                const zapatillaId = card.getAttribute('data-zapatilla-id');
                const zapatilla = zapatillasHombre.find(zapatilla => zapatilla.id === parseInt(zapatillaId));
                mostrarDetallesZapatilla(zapatilla);
            });
        });
    })
    .catch(error => console.log(error));

    function mostrarDetallesZapatilla(zapatilla) {
        const modalTitle = document.getElementById('zapatillaModalLabel');
        const modalBody = document.getElementById('zapatillaDetalle');
        modalTitle.textContent = zapatilla.nombre;
        modalBody.innerHTML = `
            <img src="${zapatilla.imagen}" class="img-fluid mb-2" alt="${zapatilla.nombre}">
            <p><b>Descripcion:</b> ${zapatilla.descripcion}</p>
            <p>Tipo: ${zapatilla.tipo}</p>
            <p>Precio: $${zapatilla.precio}</p>
        `;
        const agregarAlCarritoBtn = document.getElementById('agregarAlCarritoBtn');
        agregarAlCarritoBtn.onclick = () => {
            agregarAlCarrito(zapatilla);
            $('#zapatillaModal').modal('hide');
        };
    }

    function agregarAlCarrito(zapatilla) {
        const itemExistente = carrito.find(item => item.id === zapatilla.id);
        if (itemExistente) {
            itemExistente.cantidad++;
        } else {
            carrito.push({...zapatilla, cantidad: 1});
        }
        mostrarAlerta();
        actualizarCarrito();
    }

    function eliminarDelCarrito(id) {
        carrito = carrito.filter(item => item.id !== id);
        actualizarCarrito();
    }

    function cambiarCantidad(id, cantidad) {
        const item = carrito.find(item => item.id === id);
        if (item) {
            item.cantidad = cantidad;
            actualizarCarrito();
        }
    }

    function actualizarCarrito() {
        const carritoBody = document.getElementById('carrito-body');
        carritoBody.innerHTML = '';
        let total = 0;
        
        carrito.forEach(item => {
            const row = document.createElement('tr');

            const nombre = document.createElement('td');
            nombre.textContent = item.nombre;

            const precio = document.createElement('td');
            precio.textContent = item.precio;

            const cantidad = document.createElement('td');
            const inputCantidad = document.createElement('input');
            inputCantidad.type = 'number';
            inputCantidad.value = item.cantidad;
            inputCantidad.min = 1;
            inputCantidad.classList.add('form-control');
            inputCantidad.addEventListener('change', () => cambiarCantidad(item.id, parseInt(inputCantidad.value)));
            cantidad.appendChild(inputCantidad);

            const subtotal = document.createElement('td');
            subtotal.textContent = item.precio * item.cantidad;

            const acciones = document.createElement('td');
            const eliminarBtn = document.createElement('button');
            eliminarBtn.classList.add('btn', 'btn-danger');
            eliminarBtn.textContent = 'Eliminar';
            eliminarBtn.addEventListener('click', () => eliminarDelCarrito(item.id));
            acciones.appendChild(eliminarBtn);

            row.appendChild(nombre);
            row.appendChild(precio);
            row.appendChild(cantidad);
            row.appendChild(subtotal);
            row.appendChild(acciones);

            carritoBody.appendChild(row);

            total += item.precio * item.cantidad;
        });

        document.getElementById('total-carrito').textContent = total;
        document.getElementById('carritoCantidad').textContent = carrito.length;
    }

    function mostrarAlerta() {
        const alertCarrito = document.getElementById('alert-carrito');
        alertCarrito.style.display = 'block';
        setTimeout(() => {
            alertCarrito.style.display = 'none';
        }, 3000);
    }
});