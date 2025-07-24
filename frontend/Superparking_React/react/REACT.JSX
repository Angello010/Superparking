<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<title>React App</title>
<!-- Cargar React y ReactDOM desde CDN -->
<script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
<!-- Babel para usar JSX -->
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
</head>
<body>
<div id="root"></div>

<!-- Tu código React -->
<script type="text/babel">
function App() {
return <h1>¡Hola desde React!</h1>;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
</script>
</body>
</html>
