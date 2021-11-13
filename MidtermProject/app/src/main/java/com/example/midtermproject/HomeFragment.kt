package com.example.midtermproject

import android.os.Bundle
import android.view.*
import androidx.fragment.app.Fragment
import androidx.databinding.DataBindingUtil
import androidx.navigation.findNavController
import androidx.navigation.ui.NavigationUI
import com.example.midtermproject.databinding.FragmentHomeBinding

class HomeFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val binding = DataBindingUtil.inflate<FragmentHomeBinding>(
            inflater,
            R.layout.fragment_home, container, false
        )
        binding.info.setOnClickListener { view: View ->
            view.findNavController().navigate(R.id.action_homeFragment_to_statisticsFragment)
        }
        binding.fertile.setOnClickListener { view: View ->
            view.findNavController().navigate(R.id.action_homeFragment_to_fertileFragment)
        }
        binding.infertile.setOnClickListener { view: View ->
            view.findNavController().navigate(R.id.action_homeFragment_to_infertileFragment)
        }
        setHasOptionsMenu(true)
        return binding.root
    }

    override fun onCreateOptionsMenu(menu: Menu, inflater: MenuInflater) {
        super.onCreateOptionsMenu(menu, inflater)
        inflater.inflate(R.menu.option_menu, menu)
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return NavigationUI.onNavDestinationSelected(item, requireView().findNavController())
                || super.onOptionsItemSelected(item)
    }
}