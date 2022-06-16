@extends('layouts.app')

@section('conteudo')
    <h1>Formulário de Contato no final da Página</h1>
    <div>
        <div class="h-96"></div>
        <div class="h-96"></div>
    </div>

    <h2 class="text-lg font-semibold">Formulário de Contato</h2>

    <livewire:form-contato />
    @endsection