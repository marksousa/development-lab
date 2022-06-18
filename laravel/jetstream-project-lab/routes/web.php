<?php

use App\Http\Livewire\HelloWorld;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::middleware(['auth:sanctum', config('jetstream.auth_session'),'verified'])
->group(function () {
    Route::get('/dashboard', function () {
        return view('dashboard');
    })->name('dashboard');
});

Route::get('/hello-world', HelloWorld::class);

Route::get('/post', function(){
    return view('livewire.post-form');
});