<?php

namespace Tests\Feature;

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Livewire\Livewire;
use Tests\TestCase;

class RegistrationTest extends TestCase
{
    use RefreshDatabase;

    /** @test */
    public function um_visitante_do_site_consegue_se_registrar()
    {
        Livewire::test('auth.register')
            ->set('email', 'mark@mark.com')
            ->set('password', 'secret')
            ->set('passwordConfirmation', 'secret')
            ->call('register')
            ->assertRedirect('/');
    }

        /** @test */
        public function nao_permite_registro_com_mesmo_email()
        {
            $user = User::create([
                'email' => 'email@email.com',
                'password' => '123456'
            ]);

            Livewire::test('auth.register')
            ->set('email', 'email@email.com')
            ->set('password', 'secret')
            ->set('passwordConfirmation', 'secret')
            ->call('register')
            ->assertHasErrors('email');
        }
}