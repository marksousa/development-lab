<?php

use App\Http\Controllers\DocumentsController;
use Illuminate\Support\Facades\Route;

Route::middleware(['web'])->group(function () {
    Route::get('documents/{document}', [DocumentsController::class, 'show']);
});

Route::get('/home', function(){
    return view('home');
});