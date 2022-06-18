<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ProfileTest extends TestCase
{
        /** @test */
        public function can_see_livewire_profile_component_on_profile_page()
        {
            $this->get('/profile')
                ->assertSuccessful()
                ->assertSeeLivewire('profile');
        }
}