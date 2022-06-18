<?php

namespace Tests\Feature;

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Hash;
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
    public function email_obrigatorio_no_registro()
    {
        Livewire::test('auth.register')
            ->set('password', 'senha123')
            ->set('passwordConfirmation', 'senha123')
            ->call('register')
            ->assertHasErrors(('email'));
    }

    /** @test */
    public function nao_permitir_email_em_branco_no_registro()
    {
        Livewire::test('auth.register')
            ->set('email', '')
            ->set('password', 'senha123')
            ->set('passwordConfirmation', 'senha123')
            ->call('register')
            ->assertHasErrors((['email' => 'required']));
    }

    /** @test */
    public function nao_permitir_registro_com_mesmo_email()
    {
        $user = User::create([
            'email' => 'email@email.com',
            'password' => Hash::make('123456'),
        ]);

        Livewire::test('auth.register')
            ->set('email', 'email@email.com')
            ->set('password', 'secret')
            ->set('passwordConfirmation', 'secret')
            ->call('register')
            ->assertHasErrors(['email' => 'unique']);
    }

    /** @test */
    public function ver_mensagem_de_erro_ao_inserir_email_ja_cadastrado_no_sistema()
    {
        $user = User::create([
            'email' => 'email@email.com.br',
            'password' => Hash::make('123456'),
        ]);

        Livewire::test('auth.register')
            ->set('email', 'email@email.com')
            ->assertHasNoErrors()
            ->set('email', 'email@email.com.br')
            ->assertHasErrors(['email' => 'unique']);
    }

    /** @test */
    public function nao_registro_sem_email_valido()
    {
        Livewire::test('auth.register')
            ->set('email', 'mark')
            ->set('password', 'segredo')
            ->set('passwordConfirmation', 'segredo')
            ->call('register')
            ->asserthasErrors(['email' => 'email']);
    }

    /** @test */
    public function confirmacao_de_senha()
    {
        Livewire::test('auth.register')
            ->set('email', 'teste@email.com')
            ->set('password', 'segredo')
            ->set('passwordConfirmation', 'nao-segredo')
            ->call('register')
            ->asserthasErrors(['password' => 'same']);
    }

    /** @test */
    public function senha_tem_no_minimo_6_caracteres()
    {
        Livewire::test('auth.register')
            ->set('email', 'teste@email.com.br')
            ->set('password', '12345')
            ->set('passwordConfirmation', '12345')
            ->call('register')
            ->asserthasErrors(['password' => 'min']);
    }
}
