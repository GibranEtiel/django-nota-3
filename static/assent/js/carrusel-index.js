document.addEventListener('DOMContentLoaded', () => {
    const url = 'https://my.api.mockaroo.com/users.json?key=e4883c10';

    fetch(url)
        .then(response => response.json())
        .then(data => {
            const carouselInner = document.getElementById('carousel-inner-custom');

            
            for (let i = 0; i < data.length; i += 3) {
                const isActive = i === 0 ? 'active' : '';
                const zapatillasGroup = data.slice(i, i + 3);

                const item = `
                    <div class="carousel-item ${isActive}">
                        <div class="row justify-content-center">
                            ${zapatillasGroup.map(zapatilla => `
                                <div class="col-md-4">
                                    <div class="card mb-4 shadow-sm" data-toggle="modal" data-target="#zapatillaModalCustom" data-zapatilla-id="${zapatilla.id}">
                                        <img src="${zapatilla.imagen}" class="card-img-top" alt="${zapatilla.nombre}">
                                        <div class="card-body">
                                            <h5 class="card-title">${zapatilla.nombre}</h5>
                                            <p class="card-text">Tipo: ${zapatilla.tipo}</p>
                                            <p class="card-text"><b>${zapatilla.precio}</b></p>
                                        </div>
                                    </div>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `;
                carouselInner.innerHTML += item;
            }

            
            document.querySelectorAll('.card').forEach(card => {
                card.addEventListener('click', () => {
                    const zapatillaId = card.getAttribute('data-zapatilla-id');
                    const zapatilla = data.find(z => z.id == zapatillaId);
                    mostrarDetallesZapatilla(zapatilla);
            
                });
            });

            
        })
        .catch(error => console.error('Error al obtener datos:', error));
});

function mostrarDetallesZapatilla(zapatilla) {
    const zapatillaDetalleCustom = document.getElementById('zapatillaDetalleCustom');
    zapatillaDetalleCustom.innerHTML = `
        <img src="${zapatilla.imagen}" class="img-fluid mb-3" alt="${zapatilla.nombre}">
        <h5>${zapatilla.nombre}</h5>
        <p><b>Descripcion:</b> ${zapatilla.descripcion}</p>
        <p>Tipo: ${zapatilla.tipo}</p>
        <p><b>Precio:</b> ${zapatilla.precio}</p>
    `;
    const zapatillaModalCustom = new bootstrap.Modal(document.getElementById('zapatillaModalCustom'));
    zapatillaModalCustom.show();
}

