<?php

use App\Http\Livewire\Register;
use Illuminate\Support\Facades\Route;

Route::get('/register', function(){
    return view('auth.register');
});

Route::get('/', function(){
    return ['success!'];
});

Route::get('/profile', function(){
    return view('profile');
});