<?php

namespace App\Http\Livewire;

use Livewire\Component;

class HelloWorld extends Component
{
    public $nome;
    public $isHuman = false;
    public $gender;

    public function mount($nome)
    {
        $this->nome = $nome;
    }

    public function render()
    {
        return view('livewire.hello-world');
    }
}