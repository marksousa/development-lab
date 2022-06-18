<?php

namespace App\Http\Livewire;

use Livewire\Component;

class HelloWorld extends Component
{

    public $message;

    public function mount()
    {
        $this->message = "Hello World!";
    }


    public function render()
    {
        return view('livewire.hello-world');
    }
}