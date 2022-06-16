<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/ ', function(){
    return view('home');
});

Route::post('/contato', function (Request $request){
    $contato = $request->validate([
        'nome' => 'required',
        'email' => 'required|email',
        'celular' => 'required',
        'mensagem' => 'required',
    ]);
});