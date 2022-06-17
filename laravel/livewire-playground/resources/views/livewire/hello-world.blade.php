<div>
    <input wire:model="nome" type="text">
    <input wire:model="isHuman" type="checkbox">
    <input wire:model="gender" value="Male" type="radio">
    <input wire:model="gender" value="Female" type="radio">
    Hello {{ $nome }}! Gender: {{ $gender }}
    @if($isHuman)
        <p>You're an human!</p>
    @endif

</div>
