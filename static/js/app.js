const routes = {
    '#login': 
        `
        <h1>Login</h1>
        <form>
            <div class="mb-3">
                <label for="ID" class="form-label">ID:</label>
                <input type="number" class="form-control" id="ID">
            </div>
            <div class="mb-3">
                <label for="username" class="form-label">Username:</label>
                <input type="name" class="form-control" id="username">
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Password:</label>
                <input type="password" class="form-control" id="password">
            </div>
            <button type="submit" class="btn btn-primary">Cadastar</button>
        </form>
        

        `,
    '#carrinho': `
        <h1>Carrinho</h1>
        <form>
            <div class="mb-3">
                <label for="IDUser" class="form-label">ID Usuário:</label>
                <input type="number" class="form-control" id="ID">
            </div>
            <div class="mb-3">
                <label for="IDProduto" class="form-label">ID Produto:</label>
                <input type="number" class="form-control" id="ID">
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Password:</label>
                <input type="password" class="form-control" id="password">
            </div>
            <button type="submit" class="btn btn-primary">Cadastar</button>
        </form>
        `,
    '#pedidos': `
        <h1>Pedidos</h1>
        <form>
            <div class="mb-3">
                <label for="ID" class="form-label">ID:</label>
                <input type="number" class="form-control" id="ID">
            </div>
            <div class="mb-3">
                <label for="username" class="form-label">Username:</label>
                <input type="name" class="form-control" id="username">
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Password:</label>
                <input type="password" class="form-control" id="password">
            </div>
            <button type="submit" class="btn btn-primary">Cadastar</button>
        </form>
        `,
    '#produtos': `
        <h1>Produtos</h1>
        <div class="mb-3">
            <label for="ID" class="form-label">ID:</label>
            <input type="number" class="form-control" id="ID">
        </div>
        <div class="mb-3">
            <label for="username" class="form-label">Username:</label>
            <input type="name" class="form-control" id="username">
        </div>
        <div class="mb-3">
            <label for="password" class="form-label">Password:</label>
            <input type="password" class="form-control" id="password">
        </div>
        <button type="submit" class="btn btn-primary">Cadastar</button>
    </form>
        `   
};

function inicio() {
    const conteudo = routes[window.location.hash] || routes['#carrinho'];
    document.getElementById('app').innerHTML = conteudo;
}

window.addEventListener('hashchange', inicio);
inicio();