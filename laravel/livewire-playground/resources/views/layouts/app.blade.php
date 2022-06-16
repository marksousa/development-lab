<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Livewire Examples</title>
    <link rel="stylesheet" href="/css/main.css">
    @livewireStyles
</head>

<body>
    <main class="container mx-auto">
        @yield('conteudo')
    </main>

    @livewireScripts
</body>

</html>
