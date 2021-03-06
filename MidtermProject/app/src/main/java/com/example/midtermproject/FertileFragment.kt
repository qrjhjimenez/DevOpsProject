package com.example.midtermproject

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.navigation.findNavController
import com.example.midtermproject.databinding.FragmentFertileBinding

class FertileFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {

        val binding = DataBindingUtil.inflate<FragmentFertileBinding>(
            inflater,
            R.layout.fragment_fertile,
            container,
            false
        )
        binding.buttonfer.setOnClickListener { view: View ->
            view.findNavController().navigate(R.id.action_fertileFragment_to_homeFragment)
        }
        return binding.root
    }
}