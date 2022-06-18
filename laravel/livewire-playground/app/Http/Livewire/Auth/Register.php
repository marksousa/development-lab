<?php

namespace App\Http\Livewire\Auth;

use App\Models\User;
use Livewire\Component;
use Illuminate\Support\Facades\Hash;

class Register extends Component
{
    public $email = '';
    public $password = '';
    public $passwordConfirmation = '';

    protected $rules = [
        'email' => 'required|email|unique:users',
        'password' => 'required|min:5|same:passwordConfirmation',
    ];

    protected $messages = [
        'email.required' => 'Digite um email.',
        'email.email' => 'Digite um email válido.',
        'email.unique' => 'Este e-mail já possui cadastro.',
        'password.required' => 'É obrigatório cadastrar uma senha',
        'password.min' => 'Sua senha deve ter ao menos 6 caracteres.',
        'password.same' => 'O campo senha e confirmação de senha devem conincidir.',
    ];

    public function register()
    {
        $data = $this->validate();
        
        User::create([
            'email' => $data['email'],
            'password' => Hash::make($data['password']),
        ]);

        return redirect('/');

    }

    // This method update all properties on self change
    // public function updated($propertyName) {
    //     $this->validateOnly($propertyName);
    // }

    public function updated()
    {
        $this->validate([
            'email' => 'required|email|unique:users',
        ]);
    }

    public function render()
    {
        return view('livewire.auth.register');
    }
}